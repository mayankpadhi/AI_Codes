clear all;
close all;

%--------------------------------------------
% Patterns to store
% D, J, C, M
%--------------------------------------------
X = [1 1 1 1 -1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 1 -1;		% D
1 1 1 1 1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 1 -1 -1 1 -1 1 1 1 -1 -1;			% J
-1 1 1 1 1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 1 1 1;		% C
1 -1 -1 -1 1 1 1 -1 1 1 1 -1 1 -1 1 1 -1 -1 -1 1 1 -1 -1 -1 1;			% M
-1 -1 1 -1 1 1 1 -1 -1 -1 1 -1 -1 -1 -1 1 -1 -1 -1 -1 -1 1 1 1 1;		% C
-1 1 -1 -1 -1 1 -1 1 -1 1 -1 -1 1 -1 1 1 -1 -1 -1 -1 -1 1 1 1 1		% C
]';

%figure;
%imshow(reshape(-X(:,1),5,5)');
%--------------------------------------------
% Learn the weights according to Hebb's rule 
%--------------------------------------------
[m,n] = size(X);
W = zeros(m,m);
for i = 1:n
	W = W + X(:,i)*X(:,i)';
endfor
W(logical(eye(size(W)))) = 0;
W = W/n;

%-------------------------------------------
% Dynamical (Linear) System and fixed points
%-------------------------------------------
x = X(:,1);               %for new char change here
x(5)=-1*x(5);
x(11)=-1*x(11);
x(2)=-1*x(2);
x(3)=-1*x(3);
#{
x(13)=-1*x(13);
x(14)=-1*x(14);
#}

figure(1);
subplot(1,2,1);
imshow(reshape(-X(:,1),5,5)');    %for new char change here
subplot(1,2,2);
imshow(reshape(-x,5,5)');

#{
y = x;
erry = 10;
while erry > 1
	yp = sign(W*y);	
	erry = norm(yp-y);
	y = yp;
  #{
	figure(2);
	imshow(reshape(-y, 5, 5)');
  #}
	pause();
endwhile
#}

%--------------------------------------------
% Damaging 50 neurons!
%--------------------------------------------
for i = 1:20
  d= randi([1, 25]);
  e= randi([1, 25]);

  #W(d, e)= 0;
  if (W(d, e)== 1)
    W(d, e)= -1;
  else
    W(d, e)= 1;
  endif
endfor

y = x;
erry = 10;
while erry > 1
	yp = sign(W*y);	
	erry = norm(yp-y);
	y = yp;
	figure(3);
	imshow(reshape(-y, 5, 5)');
	%pause();
endwhile