import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import StrengthMeter from "../components/StrengthMeter";

describe("StrengthMeter", () => {
  it("renders the strength label and entropy", () => {
    render(<StrengthMeter strength="Strong" score={82} entropyBits={78.4} crackTime="12.3 years" />);

    expect(screen.getByText("Strong")).toBeInTheDocument();
    expect(screen.getByText("78.4 bits of entropy")).toBeInTheDocument();
    expect(screen.getByText("12.3 years")).toBeInTheDocument();
  });

  it("renders nothing when no strength is provided", () => {
    const { container } = render(<StrengthMeter strength={null} score={0} entropyBits={0} crackTime="" />);
    expect(container).toBeEmptyDOMElement();
  });
});
