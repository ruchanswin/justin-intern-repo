import { add } from "./Calculations";
import { subtract } from "./Calculations";
import { multiply } from "./Calculations";
import { divide } from "./Calculations";

test("perform natural number calculations", () => {
  expect(add(2, 3)).toBe(5);
  expect(subtract(5, 2)).toBe(3);
  expect(multiply(2, 3)).toBe(6);
  expect(divide(6, 2)).toBe(3);
});

test("perform negative numbers", () => {
  expect(add(-1, -6)).toBe(-7);
  expect(subtract(-5, -2)).toBe(-3);
  expect(multiply(-2, -3)).toBe(6);
  expect(divide(-6, -2)).toBe(3);
});

test("perform zero", () => {
  expect(add(0, 5)).toBe(5);
  expect(subtract(5, 0)).toBe(5);
  expect(multiply(0, 3)).toBe(0);
  expect(divide(0, 2)).toBe(0);
});

test("perform floating point numbers", () => {
  expect(add(2.5, 3.5)).toBeCloseTo(6.0);
  expect(subtract(5.5, 2.5)).toBeCloseTo(3.0);
  expect(multiply(2.5, 3.5)).toBeCloseTo(8.75);
  expect(divide(7.5, 2.5)).toBeCloseTo(3.0);
});
