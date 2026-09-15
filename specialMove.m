function [] = specialMove(s)
%% moves plate in a fibonacci sequence
    i = 1;
    x = [1 1 2 3 5];
    while i <= 4
        writeline(s,sprintf('MOVE %d %d', x(i), x(i+1))); % sprintf allows index var to be a part of the string
    i =+ 1;
    end

end