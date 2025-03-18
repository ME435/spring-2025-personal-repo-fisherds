classdef Beer
    
    properties
        AlcoholPercentage % Alcohol by volume (ABV)
        SizeOz % Size of beer in ounces
        IsFull = true % Whether the beer is full or empty
    end
    
    methods
        function obj = Beer(alcoholPercentage, sizeOz)
            obj.AlcoholPercentage = alcoholPercentage;
            obj.SizeOz = sizeOz;
        end
        
        function obj = drink(obj)
            if obj.IsFull
                obj.IsFull = false;
%                 fprintf('The beer (%.1f%% ABV, %.1f oz) has been consumed!\n', obj.AlcoholPercentage, obj.SizeOz);
            else
                fprintf('The beer is already empty!\n');
            end
        end
        
        function obj = refill(obj)
            obj.IsFull = true;
%             fprintf('The beer has been refilled!\n');
        end
    end
end

