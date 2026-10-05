function response = fibonacciMoveRemote(s, port)
%% moves plate in a fibonacci sequence
    %i = 1;
    %x = [1 1 2 3 5];
    %while i <= 4
        %writeline(s,sprintf('MOVE %d %d', x(i), x(i+1))); % sprintf allows index var to be a part of the string
    % =+ 1;
    %end

% Set up output
portnum = num2str(port);
s = (s + portnum + "/api/");

% Move 1 to 1
webread(s + 'RESET');
pause(5);
uiwait(helpdlg('Please remove all plates from the machine'));
webread(s + 'X-AXIS 1');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
uiwait(helpdlg('Please place a plate in the gripper'));
webread(s + 'GRIPPER CLOSE');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);

% Move 1 to 2
webread(s + 'X-AXIS 1');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
webread(s + 'GRIPPER CLOSE');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);
webread(s + 'X-AXIS 2');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);

% Move 2 to 3
webread(s + 'X-AXIS 2');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
webread(s + 'GRIPPER CLOSE');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);
webread(s + 'X-AXIS 3');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);

% Move 3 to 5
webread(s + 'X-AXIS 3');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
webread(s + 'GRIPPER CLOSE');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);
webread(s + 'X-AXIS 5');
pause(5);
webread(s + 'Z-AXIS EXTEND');
pause(5);
webread(s + 'GRIPPER OPEN');
pause(5);
webread(s + 'Z-AXIS RETRACT');
pause(5);
response = 'Sequence Complete';
end