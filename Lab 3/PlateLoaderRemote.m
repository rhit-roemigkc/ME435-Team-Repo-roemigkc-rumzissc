classdef PlateLoaderRemote < hgsetget
    %PLATELOADER Controls the Beckman Coulter Plate Loader Robot
    %   Performs the basic actions to control the plate loader

    properties
        serialRobot
        xAxisPosition
        isZAxisExtended
        isGripperClosed
        isPlatePresent
    end
    properties (Constant = true)
        defaultTimeTable = [0 60 20 30 0
            0 0 30 30 0
            0 30 0 30 0
            0 30 30 0 0
            0 30 20 60 0];
    end

    methods
        function obj = PlateLoaderRemote(port)
            % Construct a PlateLoader Object
            URL = ("http://137.112.225.185:");

%            portStr = '/dev/cu.usbserial-110'; % ignore the portNumber for my Mac

            obj.serialRobot = URL;
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + "/api/INITIALIZE");
            % Had to print the response since a construct cannot return mulitple items
            fprintf('%s\n', response);
            obj.xAxisPosition = 3;
            obj.isZAxisExtended = false;
            obj.isGripperClosed = true;
            % TODO: When turned on there might be a plate present
            %   Can someone add code to get Plate status
            %   Maybe use the GRIPPER_STATUS command and ready string reply
            obj.isPlatePresent = false;
        end
        function response = specialMove(obj, port)
            response = fibonacciMove(obj.serialRobot, port);
            fprintf('%s\n', response);
        end
        function response = reset(obj, port)
            % Reset robot
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + '/api/RESET');
            fprintf('%s\n', response);
            obj.xAxisPosition = 3;
            obj.isZAxisExtended = false;
            obj.isGripperClosed = true;
        end
        function response = x(obj, pos, port)
            % Moves the x-axis to position, passes the reply back to caller
            if (pos <1 || pos>5)
                response = 'Illegal position\n';
                fprintf('%s\n', response);
                return
            end
            xCommand = sprintf('/api/X-AXIS %d',pos);
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + xCommand);
            fprintf('%s\n', response);
            if(obj.xAxisPosition ~= pos)
                obj.isZAxisExtended = false;
            end
            obj.xAxisPosition = pos;
        end
        function response = extend(obj, port)
            % Extends the Z-Axis, passes the reply back to caller
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + '/api/Z-AXIS EXTEND');
            fprintf('%s\n', response);
            
            if startsWith(response, "ERROR")
                obj.isZAxisExtended = false;
            else
                obj.isZAxisExtended = true;
            end
        end
        function response = retract(obj, port)
            % Retracts the Z-Axis, passes the reply back to caller
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + '/api/Z-AXIS RETRACT');
            obj.isZAxisExtended = false;
            fprintf('%s\n', response);
        end
        function response = close(obj, port)
            % Close Gripper, passes the reply back to caller
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + '/api/GRIPPER CLOSE');
            obj.isGripperClosed = true;
            if endsWith(response, "NOPLATE")
                obj.isPlatePresent = false;
            else
                obj.isPlatePresent = true;
            end
            fprintf('%s\n', response);
        end
        function response = open(obj, port)
            % Open Gripper, passes the reply back to caller
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + '/api/GRIPPER OPEN');
            obj.isGripperClosed = false;
            obj.isPlatePresent = false;
            fprintf('%s\n', response);
        end
        function response = movePlate(obj, startPos, endPos, port)
            % movePlate(startPos, endPos)- Passes two MATLAB numbers for the
            % start and end position of the plate, tries to move the plate to
            % that position, and passes the reply back to caller
            if (startPos <1 || startPos>5 || endPos <1 || endPos>5)
                response = 'Illegal position\n';
                fprintf('%s\n', response);
                return
            end
            portstr = num2str(port);
            moveCommand = sprintf('/api/MOVE %d %d',startPos,endPos);
            response = webread(obj.serialRobot + portstr + moveCommand);
            fprintf('%s\n', response);

            if startsWith(response, "ERROR")
                obj.xAxisPosition = startPos;
                obj.isZAxisExtended = false;
                obj.isGripperClosed = false;
                obj.isPlatePresent = false;
            else
                obj.xAxisPosition = 3;
                obj.isZAxisExtended = false;
                obj.isGripperClosed = true;
                obj.isPlatePresent = false;
            end
        end
        function response = setTimeValues(obj, timeDelays, port)
            % setTimeValues(timeDelays) - Passes a matrix with 5 rows (froms)
            % and 5 columns (tos) to set all the time delay value
            if (~isequal(size(timeDelays), [5 5]))
                response = 'Need a 5 by 5 matrix of time delays\n';
                fprintf('%s\n', response);
                return
            end
            portstr = num2str(port);
            for i = 1:5
                for j = 2:4
                    if(i ~= j)
                        timeCommand = sprintf('/api/SET_DELAY %d %d %d', i,j,timeDelays(i,j));
                        response = webread(obj.serialRobot + portstr + timeCommand);
                        fprintf('%s\n', response);
                    end
                end
            end
        end
        function response = resetDefaultTimes(obj, port)
            % Resets the default time delay table values
            response = obj.setTimeValues(obj.defaultTimeTable, port);
        end
        function response = getStatus(obj, port)
            % Since we are keeping the status as instance fields we can just
            % get the properties of the class, this is a useful double check
            % TODO: Make the values update if different
            %  Can someone make the call to LOADED_STATUS also update
            %  properties, just in case somehow it gets off
            portstr = num2str(port);
            response = webread(obj.serialRobot + portstr + '/api/LOADER_STATUS');
            fprintf('%s\n', response);
        end

        % Other to todo's if someone wants to.  Implement the additional
        %  weird commands: STOP_CYLINDER, VERSION,
        %  X-AXIS_STATUS, Z-AXIS_STATUS, GRIPPER_STATUS

        function [xPos,zAxis,grip,plate] = getProperties(obj)
            % Returns the status properties of the robot (for GUI display)
            xPos = obj.xAxisPosition;
            zAxis = obj.isZAxisExtended;
            grip = obj.isGripperClosed;
            plate = obj.isPlatePresent;
        end
        function response = shutdown(obj)
            % Close serial object
            delete(obj.serialRobot);
            obj.serialRobot = [];
            response = 'Disconnected';
        end
        function disp(obj)
            % Overrides the display when seeing robot status
            % Note: if you need to see the field names use
            %    get(_objectName_)
            fprintf('  X-AXIS %d, ',obj.xAxisPosition);
            if (obj.isZAxisExtended)
                fprintf('EXTENDED, ');
            else
                fprintf('RETRACTED, ');
            end
            if (obj.isGripperClosed)
                if( obj.isPlatePresent )
                    fprintf('CLOSED, PLATE');
                else
                    fprintf('CLOSED, NOPLATE');
                end
            else
                fprintf('OPEN');
            end
            fprintf('\n');
        end
    end
end
