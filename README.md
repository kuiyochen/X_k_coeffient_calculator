# X_k_coeffient_calculator
The coefficient calculating algorithm decribed in the paper

### Ex:
For $k = 3$,
$$A[1;1]**3/6 - A[1;1]*A[1;2]/2 + A[1;1]*A[2;1] - A[1;1|2;1] + A[1;3]/3 + A[3;1]$$
means
$$
+\left(\sum\limits_{n=1}^{\infty}a_{n,1}\right)^3/6
-\left(\sum\limits_{n=1}^{\infty}a_{n,1}\right)\left(\sum\limits_{n=1}^{\infty}a_{n,1}^2\right)/2
+\left(\sum\limits_{n=1}^{\infty}a_{n,1}\right)\left(\sum\limits_{n=1}^{\infty}a_{n,2}\right)
-\left(\sum\limits_{n=1}^{\infty}a_{n,1}a_{n,2}\right)
+\left(\sum\limits_{n=1}^{\infty}a_{n,1}^3\right)/3
+\left(\sum\limits_{n=1}^{\infty}a_{n,3}\right).
$$
