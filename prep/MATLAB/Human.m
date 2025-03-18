
classdef Human
    properties
        Name % Name of the person
        BAC = 0 % Blood Alcohol Content (initially 0)
    end
    
    methods
        function obj = Human(name)
            obj.Name = name;
        end
        
        function obj = drink(obj, beer)
            if beer.IsFull
                obj.BAC = obj.BAC + (beer.AlcoholPercentage / 100) * beer.SizeOz * 0.05;
                fprintf('%s drank a beer (%.1f%% ABV, %.1f oz). BAC is now %.3f\n', obj.Name, beer.AlcoholPercentage, beer.SizeOz, obj.BAC);
            else
                fprintf('%s tried to drink, but the beer is empty!\n', obj.Name);
            end
        end
        
        function obj = hour_passes(obj)
            obj.BAC = max(obj.BAC - 0.015, 0); % BAC decreases by 0.015 per hour
            fprintf('An hour passed. %s''s BAC is now %.3f\n', obj.Name, obj.BAC);
        end
        
        function drunk = is_drunk(obj)
            drunk = obj.BAC >= 0.08;
            if drunk
                fprintf('%s is drunk!\n', obj.Name);
            else
                fprintf('%s is sober.\n', obj.Name);
            end
        end
    end
end