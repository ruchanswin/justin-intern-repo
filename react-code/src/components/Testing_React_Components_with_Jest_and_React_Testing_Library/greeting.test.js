import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";
import Greeting from "./Greeting";

test("displays initial welcome message", () => {
  render(<Greeting />);
  expect(screen.getByText("Welcome to Focus Bear!")).toBeInTheDocument();
});

test("displays greeting message after clicking the button", () => {
  render(<Greeting />);
  fireEvent.click(screen.getByText("Greeting"));
  expect(screen.getByText("Hello Justin!")).toBeInTheDocument();
});
