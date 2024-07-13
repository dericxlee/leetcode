/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    let array = [];
    
    for (let i = 0 ; i < matrix.length; i++) {
        for (let j = 0; j < matrix.length; j++) {
            array.push(matrix[i][j]);
        }
    }
    
    for (let i = 0 ; i < matrix.length; i++) {
        for (let j = 0; j < matrix.length; j++) {
            matrix[j][i] = array.shift();
        }
    }
    
    for (let i = 0 ; i < matrix.length; i++) {
       matrix[i] = matrix[i].reverse();
    }

    return matrix;
};