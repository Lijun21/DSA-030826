import { useState, useEffect } from "react";

const WORDS = ["ball", "asee", "let", "lep"];

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export default function App() {
  const [step, setStep] = useState(null);
  const [history, setHistory] = useState([]);
  const [running, setRunning] = useState(false);
  const [done, setDone] = useState(false);
  const [result, setResult] = useState(null);

  const grid = WORDS;
  const maxCols = Math.max(...WORDS.map((w) => w.length));

  const getChar = (r, c) => (c < grid[r]?.length ? grid[r][c] : null);

  const reset = () => {
    setStep(null);
    setHistory([]);
    setRunning(false);
    setDone(false);
    setResult(null);
  };

  const run = async () => {
    reset();
    await sleep(100);
    setRunning(true);
    const log = [];

    for (let row = 0; row < grid.length; row++) {
      for (let col = 0; col < grid[row].length; col++) {
        const a = getChar(row, col);
        const b = getChar(col, row);
        const match = b !== null && a === b;

        const current = { row, col, a, b, match };
        setStep(current);
        log.push({ ...current });
        setHistory([...log]);
        await sleep(800);

        if (!match) {
          setResult(false);
          setDone(true);
          setRunning(false);
          return;
        }
      }
    }

    setResult(true);
    setDone(true);
    setRunning(false);
  };

  const colLabels = Array.from({ length: maxCols }, (_, i) => i);

  return (
    <div style={{
      minHeight: "100vh",
      background: "#0d0d0d",
      color: "#e8e8e8",
      fontFamily: "'Courier New', monospace",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      padding: "40px 20px",
    }}>
      <div style={{ fontSize: 11, letterSpacing: 6, color: "#555", marginBottom: 8, textTransform: "uppercase" }}>
        Valid Word Square
      </div>
      <h1 style={{ fontSize: 26, fontWeight: 700, margin: "0 0 40px", color: "#fff", letterSpacing: 1 }}>
        words[row][col] == words[col][row]
      </h1>

      {/* Grid */}
      <div style={{ display: "flex", flexDirection: "column", gap: 4, marginBottom: 40 }}>
        {/* Col index headers */}
        <div style={{ display: "flex", gap: 4, paddingLeft: 32 }}>
          {colLabels.map((c) => (
            <div key={c} style={{
              width: 52, height: 28, display: "flex", alignItems: "center", justifyContent: "center",
              fontSize: 11, color: "#444", letterSpacing: 1,
            }}>col {c}</div>
          ))}
        </div>

        {grid.map((word, r) => (
          <div key={r} style={{ display: "flex", gap: 4, alignItems: "center" }}>
            <div style={{ width: 28, fontSize: 11, color: "#444", textAlign: "right", paddingRight: 4 }}>r{r}</div>
            {Array.from({ length: maxCols }, (_, c) => {
              const char = getChar(r, c);
              const isRowActive = step && step.row === r && step.col === c;
              const isColActive = step && step.col === r && step.row === c;
              const isActive = isRowActive || isColActive;

              let bg = "#1a1a1a";
              let border = "1px solid #2a2a2a";
              let color = "#555";
              let scale = 1;

              if (char !== null) {
                bg = "#1e1e1e";
                border = "1px solid #333";
                color = "#aaa";
              }

              if (isActive && step) {
                if (isRowActive) {
                  bg = step.match ? "#0d3320" : "#3a0d0d";
                  border = step.match ? "2px solid #00e676" : "2px solid #ff4444";
                  color = step.match ? "#00e676" : "#ff4444";
                  scale = 1.1;
                } else {
                  bg = step.match ? "#0a2a1a" : "#2a0a0a";
                  border = step.match ? "2px solid #00a854" : "2px solid #cc2222";
                  color = step.match ? "#00a854" : "#cc2222";
                  scale = 1.1;
                }
              }

              return (
                <div key={c} style={{
                  width: 52, height: 52,
                  background: bg,
                  border,
                  borderRadius: 6,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontSize: char ? 22 : 12,
                  fontWeight: 700,
                  color,
                  transform: `scale(${scale})`,
                  transition: "all 0.3s ease",
                  position: "relative",
                }}>
                  {char ?? (r < maxCols && c < grid.length ? "—" : "")}
                  {isRowActive && <div style={{
                    position: "absolute", top: -14, fontSize: 9,
                    color: step.match ? "#00e676" : "#ff4444", letterSpacing: 1
                  }}>row</div>}
                  {isColActive && <div style={{
                    position: "absolute", bottom: -14, fontSize: 9,
                    color: step.match ? "#00a854" : "#cc2222", letterSpacing: 1
                  }}>col</div>}
                </div>
              );
            })}
          </div>
        ))}
      </div>

      {/* Comparison panel */}
      <div style={{
        width: 360,
        background: "#111",
        border: "1px solid #222",
        borderRadius: 10,
        padding: "20px 24px",
        marginBottom: 32,
        minHeight: 90,
      }}>
        {step ? (
          <>
            <div style={{ fontSize: 12, color: "#555", marginBottom: 10, letterSpacing: 2 }}>CHECKING</div>
            <div style={{ display: "flex", alignItems: "center", gap: 16, justifyContent: "center" }}>
              <div style={{ textAlign: "center" }}>
                <div style={{ fontSize: 11, color: "#555", marginBottom: 4 }}>words[{step.row}][{step.col}]</div>
                <div style={{
                  fontSize: 32, fontWeight: 800,
                  color: step.match ? "#00e676" : "#ff4444",
                }}>'{step.a}'</div>
              </div>
              <div style={{ fontSize: 20, color: step.match ? "#00e676" : "#ff4444" }}>
                {step.match ? "==" : "!="}
              </div>
              <div style={{ textAlign: "center" }}>
                <div style={{ fontSize: 11, color: "#555", marginBottom: 4 }}>words[{step.col}][{step.row}]</div>
                <div style={{
                  fontSize: 32, fontWeight: 800,
                  color: step.match ? "#00e676" : "#ff4444",
                }}>'{step.b ?? "?"}'</div>
              </div>
            </div>
          </>
        ) : (
          <div style={{ color: "#333", textAlign: "center", paddingTop: 20, fontSize: 13 }}>
            Hit Run to start the visualization
          </div>
        )}
      </div>

      {/* History log */}
      {history.length > 0 && (
        <div style={{
          width: 360,
          background: "#0d0d0d",
          border: "1px solid #1e1e1e",
          borderRadius: 10,
          padding: "16px 20px",
          marginBottom: 28,
          maxHeight: 180,
          overflowY: "auto",
        }}>
          <div style={{ fontSize: 11, color: "#444", letterSpacing: 2, marginBottom: 10 }}>TRACE LOG</div>
          {history.map((h, i) => (
            <div key={i} style={{
              fontSize: 12,
              color: h.match ? "#3a7a5a" : "#7a3a3a",
              padding: "3px 0",
              borderBottom: "1px solid #161616",
              fontFamily: "monospace",
            }}>
              <span style={{ color: "#444" }}>words[{h.row}][{h.col}]</span>
              {" "}<span style={{ color: h.match ? "#00a854" : "#cc3333" }}>'{h.a}' {h.match ? "==" : "!="} '{h.b ?? "?"}'</span>
              {" "}<span style={{ color: "#444" }}>← words[{h.col}][{h.row}]</span>
              {" "}{h.match ? "✓" : "✗ FAIL"}
            </div>
          ))}
        </div>
      )}

      {/* Result */}
      {done && (
        <div style={{
          fontSize: 18,
          fontWeight: 700,
          padding: "14px 36px",
          borderRadius: 8,
          background: result ? "#0d2e1a" : "#2e0d0d",
          border: `2px solid ${result ? "#00e676" : "#ff4444"}`,
          color: result ? "#00e676" : "#ff4444",
          letterSpacing: 2,
          marginBottom: 24,
        }}>
          {result ? "✓ VALID WORD SQUARE" : "✗ INVALID — return False"}
        </div>
      )}

      {/* Controls */}
      <div style={{ display: "flex", gap: 12 }}>
        <button onClick={run} disabled={running} style={{
          padding: "12px 32px",
          background: running ? "#1a1a1a" : "#fff",
          color: running ? "#444" : "#000",
          border: "none",
          borderRadius: 6,
          fontFamily: "monospace",
          fontWeight: 700,
          fontSize: 13,
          cursor: running ? "not-allowed" : "pointer",
          letterSpacing: 1,
          transition: "all 0.2s",
        }}>
          {running ? "Running..." : "▶ Run"}
        </button>
        <button onClick={reset} style={{
          padding: "12px 24px",
          background: "transparent",
          color: "#555",
          border: "1px solid #333",
          borderRadius: 6,
          fontFamily: "monospace",
          fontSize: 13,
          cursor: "pointer",
          letterSpacing: 1,
        }}>
          Reset
        </button>
      </div>
    </div>
  );
}

