import reducer, {
  increment,
  incrementByAmount,
  fetchDummyData,
} from "./counterSlice";

describe("counter reducer", () => {
  it("Return to the initial state", () => {
    expect(reducer(undefined, { type: undefined })).toEqual({
      value: 0,
      status: "ready",
    });
  });

  it("Handle increment", () => {
    const state = reducer({ value: 0, status: "ready" }, increment());
    expect(state.value).toBe(1);
  });

  it("Handle incrementByAmount", () => {
    const state = reducer({ value: 2, status: "ready" }, incrementByAmount(5));
    expect(state.value).toBe(7);
  });

  it("Handle fetchDummyData.fulfilled", () => {
    const action = {
      type: fetchDummyData.fulfilled.type,
      payload: 5,
    };
    const state = reducer({ value: 2, status: "pending" }, action);
    expect(state.status).toBe("completed");
    expect(state.value).toBe(7);
  });
});
