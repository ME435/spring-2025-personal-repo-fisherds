function [A1, A2, A3] = create_AdeeptArm_A_matrices(jointAngles)
% Create the A matrices for the arm.

A1 = create_A_matrix(64, 0, 0, jointAngles(1));
A2 = create_A_matrix(0, 0, -90, jointAngles(2));
A3 = create_A_matrix(0, 140, 0, jointAngles(3));

end