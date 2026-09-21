function [] = plateLoaderMenuControl(s)
while(1)
    clc
    switch(menu('Choose Command','Reset','X-Axis','Z-Axis','Gripper', ...
            'Move','Status','Special Moves','Exit'))
        case 1
            writeline(s,'RESET');
        case 2
            switch(menu('X-Axis','1','2','3','4','5'))
                case 1
                    writeline(s,'X-AXIS 1');
                case 2
                    writeline(s,'X-AXIS 2');
                case 3
                    writeline(s,'X-AXIS 3');
                case 4
                    writeline(s,'X-AXIS 4');
                case 5
                    writeline(s,'X-AXIS 5');
            end
        case 3
            switch(menu('Z-Axis','Extend','Retract'))
                case 1
                    writeline(s,'Z-AXIS EXTEND');
                case 2
                    writeline(s,'Z-AXIS RETRACT');
            end
        case 4
            switch(menu('Gripper','Open','Close'))
                case 1
                    writeline(s,'GRIPPER OPEN');
                case 2
                    writeline(s,'GRIPPER CLOSE');
            end
        case 5
            switch(menu('Move From','1','2','3','4','5'))
                case 1
                    switch(menu('Move To','2','3','4','5'))
                        case 1
                            writeline(s,'MOVE 1 2');
                        case 2
                            writeline(s,'MOVE 1 3');
                        case 3
                            writeline(s,'MOVE 1 4');
                        case 4
                            writeline(s,'MOVE 1 5');
                    end
                case 2
                    switch(menu('Move To','1','3','4','5'))
                        case 1
                            writeline(s,'MOVE 2 1');
                        case 2
                            writeline(s,'MOVE 2 3');
                        case 3
                            writeline(s,'MOVE 2 4');
                        case 4
                            writeline(s,'MOVE 2 5');
                    end
                case 3
                    switch(menu('Move To','1','2','4','5'))
                        case 1
                            writeline(s,'MOVE 3 1');
                        case 2
                            writeline(s,'MOVE 3 2');
                        case 3
                            writeline(s,'MOVE 3 4');
                        case 4
                            writeline(s,'MOVE 3 5');
                    end
                case 4
                    switch(menu('Move To','1','2','3','5'))
                        case 1
                            writeline(s,'MOVE 4 1');
                        case 2
                            writeline(s,'MOVE 4 2');
                        case 3
                            writeline(s,'MOVE 4 3');
                        case 4
                            writeline(s,'MOVE 1 5');
                    end
                case 5
                    switch(menu('Move To','1','2','3','4'))
                        case 1
                            writeline(s,'MOVE 5 1');
                        case 2
                            writeline(s,'MOVE 5 2');
                        case 3
                            writeline(s,'MOVE 5 3');
                        case 4
                            writeline(s,'MOVE 5 4');
                    end
            end
        case 6
            writeline(s,'LOADER_STATUS');
        case 7
            specialMove(s);
        case 8
            fprintf('Goodbye\n')
            break
    end
    result = readline(s)
    if ~startsWith(result,'R')
        fprintf('An error has occured, terminating program\n')
        break
    end
end