import "@testing-library/jest-dom";
import { render, screen, waitFor } from "@testing-library/react";
import UserList from "./users";
import * as api from "./api";

jest.mock("./api");

describe("UserList component", () => {
  test("displays users after successful API call", async () => {
    api.fetchUsers.mockResolvedValue([
      { id: 1, name: "Jeremy Nagel" },
      { id: 2, name: "Justin Nguyen" },
      { id: 3, name: "Bang Luong Huynh" },
      { id: 4, name: "Ben Pham" },
    ]);

    render(<UserList />);

    await waitFor(() => {
      expect(screen.getByText("Jeremy Nagel")).toBeInTheDocument();
      expect(screen.getByText("Justin Nguyen")).toBeInTheDocument();
      expect(screen.getByText("Bang Luong Huynh")).toBeInTheDocument();
      expect(screen.getByText("Ben Pham")).toBeInTheDocument();
    });
  });

  test("displays error on failed API call", async () => {
    api.fetchUsers.mockRejectedValue(new Error("API failed"));

    render(<UserList />);

    await waitFor(() => {
      expect(screen.getByText("Failed to load users")).toBeInTheDocument();
    });
  });
});
