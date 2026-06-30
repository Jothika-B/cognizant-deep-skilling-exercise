const Calculator = require("./calculator");

describe("Calculator - TDD Example", () => {
    let calculator;

    beforeEach(() => {
        calculator = new Calculator();
    });

    test("should add two numbers", () => {
        expect(calculator.add(5, 3)).toBe(8);
    });

    test("should subtract two numbers", () => {
        expect(calculator.subtract(10, 4)).toBe(6);
    });

    test("should multiply two numbers", () => {
        expect(calculator.multiply(2, 6)).toBe(12);
    });

    test("should divide two numbers", () => {
        expect(calculator.divide(8, 2)).toBe(4);
    });

    test("should throw error when dividing by zero", () => {
        expect(() => calculator.divide(5, 0))
            .toThrow("Cannot divide by zero");
    });
});
