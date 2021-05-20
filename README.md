# Human-like-constrained-mating-GA
This is the implementation of HLCMGA to optimize Canonical GA and avoid quick trapped Genetic Algorithm at local minimum. HLCM-GA give constrained in parents selection phase.

## Schema
<img src="https://i.ibb.co/1vtzWv9/flag.png" width="300" />
Every individual have two flags, the first one for gender and the other flag for genetic relationship. 
If both individual have diferent gender and not from same parents then crossover occur.

### Parents Selection Constrained
<img src="https://i.ibb.co/mhhxmzn/family-Tree.png" width="500" />
Genetic relationship flag added to offspring from their parents. Prohibited offspring are from the same parents or parents-child to do crossover.

## Benchmark Function
To test the performance of HLCMGA, the algorithm run into 10 benchmark function bellow and compare it with the performance of Canonical GA and Rao Alogorithm. 

|No.             |Function        |Mathematical Definition        |
|----------------|----------------|---------------|
|1               |Beale|<img src="https://i.upmath.me/svg/f(x%2C%20y)%20%3D%20(1.5-x%2Bxy)%5E2%2B(2.25-x%2Bxy%5E2)%5E2%2B(2.625-x%2Bxy%5E3)%5E2" alt="f(x, y) = (1.5-x+xy)^2+(2.25-x+xy^2)^2+(2.625-x+xy^3)^2" />|
|2               |Bohanchevsky|<img src="https://i.upmath.me/svg/f(x%2C%20y)%20%3D%20x%5E2%20%2B%202y%5E2%20-0.3cos(3%5Cpi%20x)-0.4cos(4%5Cpi%20y)%2B0.7" alt="f(x, y) = x^2 + 2y^2 -0.3cos(3\pi x)-0.4cos(4\pi y)+0.7" />|
|3               |Drop Wave|<img src="https://i.upmath.me/svg/f(x%2C%20y)%20%3D%20-%20%5Cfrac%7B1%20%2B%20cos(12%5Csqrt%7Bx%5E%7B2%7D%20%2B%20y%5E%7B2%7D%7D)%7D%7B(0.5(x%5E%7B2%7D%20%2B%20y%5E%7B2%7D)%20%2B%202)%7D" alt="f(x, y) = - \frac{1 + cos(12\sqrt{x^{2} + y^{2}})}{(0.5(x^{2} + y^{2}) + 2)}" />|
|4               |easom|<img src="https://i.upmath.me/svg/f(x%2Cy)%3D%E2%88%92cos(x)cos(y)%20exp(%E2%88%92(x%20%E2%88%92%20%5Cpi)%5E2%E2%88%92(y%20%E2%88%92%20%5Cpi)%5E2)" alt="f(x,y)=−cos(x)cos(y) exp(−(x − \pi)^2−(y − \pi)^2)" />|
|5               |Egg Create|<img src="https://i.upmath.me/svg/f(x%2Cy)%3Dx%5E2%20%2B%20y%5E2%20%2B%2025(sin%5E2(x)%20%2B%20sin%5E2(y))" alt="f(x,y)=x^2 + y^2 + 25(sin^2(x) + sin^2(y))" />|
|6               |Schaffer N3|<img src="https://i.upmath.me/svg/f(x%2C%20y)%3D0.5%20%2B%20%5Cfrac%7Bsin%5E2(cos(%7Cx%5E2-y%5E2%7C))-0.5%7D%7B(1%2B0.001(x%5E2%2By%5E2))%5E2%7D" alt="f(x, y)=0.5 + \frac{sin^2(cos())-0.5}{(1+0.001(x^2+y^2))^2}" />|
|7               |Kaene|<img src="https://i.upmath.me/svg/f(x%2Cy)%3D-%5Cfrac%7B%5Csin%5E2(x-y)%5Csin%5E2(x%2By)%7D%7B%5Csqrt%7Bx%5E2%2By%5E2%7D%7D" alt="f(x,y)=-\frac{\sin^2(x-y)\sin^2(x+y)}{\sqrt{x^2+y^2}}" />|
|8               |Bird|<img src="https://i.upmath.me/svg/f(x%2C%20y)%20%3D%20sin(x)e%5E%7B(1-cos(y))%5E2%7D%2Bcos(y)e%5E%7B(1-sin(x))%5E2%7D%2B(x-y)%5E2" alt="f(x, y) = sin(x)e^{(1-cos(y))^2}+cos(y)e^{(1-sin(x))^2}+(x-y)^2" />|
|9               |Bartels Conn          |<img src="https://i.upmath.me/svg/f(x%2Cy)%3D%7Cx%5E2%20%2B%20y%5E2%20%2B%20xy%7C%20%2B%20%7Csin(x)%7C%20%2B%20%7Ccos(y)%7C" alt="f(x,y)= + " />|
|10              |Ackley N3          | <img src="https://i.upmath.me/svg/f(x%2C%20y)%20%3D%20-200e%5E%7B-0.2%5Csqrt%7Bx%5E2%20%2B%20y%5E2%7D%7D%20%2B%205e%5E%7Bcos(3x)%20%2B%20sin(3y)%7D" alt="f(x, y) = -200e^{-0.2\sqrt{x^2 + y^2}} + 5e^{cos(3x) + sin(3y)}" /> |

