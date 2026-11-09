import { describe, expect, it, vi } from "vitest";
import { copyToClipboard } from "../utils/clipboard";

describe("copyToClipboard", () => {
  it("uses the async Clipboard API when available", async () => {
    const writeText = vi.fn().mockResolvedValue(undefined);
    Object.assign(navigator, { clipboard: { writeText } });
    Object.defineProperty(window, "isSecureContext", { value: true, configurable: true });

    const result = await copyToClipboard("hunter2");

    expect(writeText).toHaveBeenCalledWith("hunter2");
    expect(result).toBe(true);
  });
});
