Matrix1 = magic(1000)
Matrix2 = magic(1000)
writematrix(Matrix1,'Matrix1.csv','Delimiter',',')
writematrix(Matrix2,'Matrix2.csv','Delimiter',',')
result = Matrix1 * Matrix2
writematrix(result,'result.csv','Delimiter',',')