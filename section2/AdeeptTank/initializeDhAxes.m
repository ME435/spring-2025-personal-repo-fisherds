function initializeDhAxes

% Begin: Setup for this stand alone version that will NOT go into the GUI.
close all
app.axes_arm = axes;  % Create a new axes and save a handle to it.
app.jointAngles = [0 0 0]; % Start at the zero angle position.
%  End : Setup for this stand alone version that will NOT go into the GUI.



% Begin: Code that can go into your GUI's StartupFcn.
clc

% Prepare the axes_arm properties
app.axes_arm.View = [90 -50];
app.axes_arm.Visible = 'off';

% Once you are in Matlab App Designer you can try these axes_arm properties too.
% These properties keep the Axes from automatically resizing (optional)
% app.axes_arm.XLim = [-160 250];
% app.axes_arm.YLim = [-250 250];
% app.axes_arm.ZLim = [-22 22];

% Create vertices for all the patches
makeStlLink("AdeeptL0.stl", app.axes_arm, [.2 .2 .2]);  % Doesn't move. No need to save a handle to it.
% Save references to the vertices of each patch, make points 4x1 not 3x1.
app.link1Patch = makeStlLink("AdeeptL1.stl", app.axes_arm, [112/255 198/255 210/255]);
app.link1Vertices = get(app.link1Patch, 'Vertices')';
app.link1Vertices(4,:) = ones(1, size(app.link1Vertices,2));

app.link2Patch = makeStlLink("AdeeptL2.stl", app.axes_arm, [198/255 172/255 20/255]);
app.link2Vertices = get(app.link2Patch, 'Vertices')';
app.link2Vertices(4,:) = ones(1, size(app.link2Vertices,2));

app.link3Patch = makeStlLink("AdeeptL3.stl", app.axes_arm, [181/255 24/255 35/255]);
app.link3Vertices = get(app.link3Patch, 'Vertices')';
app.link3Vertices(4,:) = ones(1, size(app.link3Vertices,2));
% End: Code that can go into your GUI's opening function.

updateArm(app);

end

function updateArm(app)

% TODO: Create the A homogeneous transformation matrices for the given jointAngles.

% TODO: Use the current A matricies to form the T0_n matricies.
% T0_1 = 
% T0_2 = 
% T0_3 = 

% TODO: Use the current T matricies to transform the original patch vertices
% link1VerticesWRTground = T0_1 * app.link1Vertices;
% link2VerticesWRTground = T0_2 * app.link2Vertices;
% link3VerticesWRTground = T0_3 * app.link3Vertices;

% TODO: Update the patches with the newly transformed vertices
% set(app.link1Patch,'Vertices', link1VerticesWRTground(1:3,:)');
% set(app.link2Patch,'Vertices', link2VerticesWRTground(1:3,:)');
% set(app.link3Patch,'Vertices', link3VerticesWRTground(1:3,:)');

end
