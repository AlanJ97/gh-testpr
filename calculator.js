class Calculator {
  add(a, b) {
    return a + b;
  }
  factorial(n) {
    return n === 0 ? 1 : n * this.factorial(n - 1);
  }
  divide(a, numerator) {
    if (numerator === 0) {
      throw new Error('Division by zero');
    }
    return a / numerator;
  }
}