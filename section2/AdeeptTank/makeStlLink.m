function p = makeStlLink(stlFilename, parentAxes, faceColor)
if (nargin == 1)
    parentAxes = gca;
    faceColor = [.7 .7 .7];
elseif (nargin == 2)
    faceColor = [.7 .7 .7];
end
set(parentAxes, 'DataAspectRatio', [1 1 1]);
stlPart = stlread(stlFilename);
p = patch('Parent', parentAxes, 'Faces',stlPart.ConnectivityList,'Vertices',stlPart.Points,'FaceColor',faceColor);

end