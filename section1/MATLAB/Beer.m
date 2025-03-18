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
        
        function obj = drink(obj)
            if obj.IsFull
                fprintf("Drank the beer\n");
                obj.IsFull = false;
            else
                fprintf("Already empty\n");
            end
        end

        function obj = refill(obj)
            obj.IsFull = true;
        end
    end
end

