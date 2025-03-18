classdef Beer < handle
    
    properties
        AlcoholPercentage
        SizeOz
        IsFull = true
    end
    
    methods
        function obj = Beer(alcoholPercentage, sizeOz)
            obj.AlcoholPercentage = alcoholPercentage;
            obj.SizeOz = sizeOz;
        end
        
        function drink(obj)
            if obj.IsFull
                fprintf("Drank the beer\n");
                obj.IsFull = false;
            else
                fprintf("This beer is already empty\n");
            end
        end

        function refill(obj)
            obj.IsFull = true;
        end
    end
end

