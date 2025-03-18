
function st_patricks_day
clc
clear
patrick = Human("Patrick");
guinness = Beer(4.2, 16); % Guinness, 4.2% ABV, 16 oz pint

% Drinking loop
for i = 1:4
    fprintf('\n--- Round %d ---\n', i);
    patrick = patrick.drink(guinness);
    guinness = guinness.drink();
    guinness = guinness.refill();
    
    patrick.is_drunk();
end

% Simulate time passing
for i = 1:5
    fprintf('\n--- %d Hour(s) Later ---\n', i);
    patrick = patrick.hour_passes();
    patrick.is_drunk();
end
end