function [] = specialMove(s)
%% moves plate in a fibonacci sequence
    %i = 1;
    %x = [1 1 2 3 5];
    %while i <= 4
        %writeline(s,sprintf('MOVE %d %d', x(i), x(i+1))); % sprintf allows index var to be a part of the string
    % =+ 1;
    %end

% Move 1 to 1
writeline(s,'RESET');
readline(s);
uiwait(helpdlg('Please remove all plates from the machine'));
writeline(s,'X AXIS 1');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
uiwait(helpdlg('Please place a plate in the gripper'));
writeline(s,'GRIPPER CLOSE');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);

% Move 1 to 2
writeline(s,'RESET');
readline(s);
writeline(s,'X AXIS 1');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
writeline(s,'GRIPPER CLOSE');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);
writeline(s,'X AXIS 2');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);

% Move 2 to 3
writeline(s,'RESET');
readline(s);
writeline(s,'X AXIS 2');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
writeline(s,'GRIPPER CLOSE');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);
writeline(s,'X AXIS 3');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);

% Move 3 to 5
writeline(s,'RESET');
readline(s);
writeline(s,'X AXIS 3');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
writeline(s,'GRIPPER CLOSE');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);
writeline(s,'X AXIS 5');
readline(s);
writeline(s,'Z-AXIS EXTEND');
readline(s);
writeline(s,'GRIPPER OPEN');
readline(s);
writeline(s,'Z-AXIS RETRACT');
readline(s);
end