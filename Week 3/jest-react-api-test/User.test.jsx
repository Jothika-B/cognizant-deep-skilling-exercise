import { render, screen, waitFor } from "@testing-library/react";
import User from "./User";

global.fetch = jest.fn();

describe("User Component", () => {
  test("renders user data from mocked API", async () => {
    fetch.mockResolvedValueOnce({
      json: async () => ({
        name: "Jothika"
      })
    });

    render(<User />);

    expect(screen.getByText("Loading...")).toBeInTheDocument();

    await waitFor(() => {
      expect(screen.getByText("Jothika")).toBeInTheDocument();
    });

    expect(fetch).toHaveBeenCalledTimes(1);
  });
});
