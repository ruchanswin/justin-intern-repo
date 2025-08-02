import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";
import Greeting from "./Greeting";

test("renders welcome message by default", () => {
  render(<Greeting />);
  expect(screen.getByText("Welcome to Focus Bear!")).toBeInTheDocument();
});

test("shows greeting message after button click", () => {
  render(<Greeting />);
  fireEvent.click(screen.getByText("Greeting"));
  expect(screen.getByText("Hello Justin!")).toBeInTheDocument();
});
