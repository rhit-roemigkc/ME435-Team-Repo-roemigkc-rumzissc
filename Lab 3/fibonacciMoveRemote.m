function response = fibonacciMoveRemote(s)
%% moves plate in a fibonacci sequence
    %i = 1;
    %x = [1 1 2 3 5];
    %while i <= 4
        %writeline(s,sprintf('MOVE %d %d', x(i), x(i+1))); % sprintf allows index var to be a part of the string
    % =+ 1;
    %end

% Move 1 to 1
webread(s + 'RESET');
pause(5);
uiwait(helpdlg('Please remove all plates from the machine'));
webread(s + 'X-AXIS 1');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
uiwait(helpdlg('Please place a plate in the gripper'));
webread(s + 'GRIPPER CLOSE');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);

% Move 1 to 2
webread(s + 'X-AXIS 1');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
webread(s + 'GRIPPER CLOSE');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);
webread(s + 'X-AXIS 2');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);

% Move 2 to 3
webread(s + 'X-AXIS 2');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
webread(s + 'GRIPPER CLOSE');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);
webread(s + 'X-AXIS 3');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);

% Move 3 to 5
webread(s + 'X-AXIS 3');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
webread(s + 'GRIPPER CLOSE');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);
webread(s + 'X-AXIS 5');
readline(s);
webread(s + 'Z-AXIS EXTEND');
readline(s);
webread(s + 'GRIPPER OPEN');
readline(s);
webread(s + 'Z-AXIS RETRACT');
readline(s);
response = 'Sequence Complete';
end