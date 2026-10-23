import sys
import json
import re

REPO_OWNER = "Jhanh"
REPO_NAME = "Jhanh"

def check_winner(b):
    lines = [
        # Rows
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Cols
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Diagonals
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    for line in lines:
        vals = [b[r][c] for r, c in line]
        if vals[0] != " " and vals[0] == vals[1] == vals[2]:
            return vals[0]
    return None

def is_full(b):
    return all(b[r][c] != " " for r in range(3) for c in range(3))

def find_best_ai_move(b):
    # 1. Can O win?
    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = "O"
                if check_winner(b) == "O":
                    b[r][c] = " "
                    return (r, c)
                b[r][c] = " "

    # 2. Block X from winning
    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = "X"
                if check_winner(b) == "X":
                    b[r][c] = " "
                    return (r, c)
                b[r][c] = " "

    # 3. Take center
    if b[1][1] == " ":
        return (1, 1)

    # 4. Take corners
    corners = [(0,0), (0,2), (2,0), (2,2)]
    for r, c in corners:
        if b[r][c] == " ":
            return (r, c)

    # 5. Take edges
    edges = [(0,1), (1,0), (1,2), (2,1)]
    for r, c in edges:
        if b[r][c] == " ":
            return (r, c)

    return None

def render_board(state):
    b = state["board"]
    winner = check_winner(b)
    game_over = winner is not None or is_full(b)

    table_rows = []
    col_headers = "| | Cột 1 | Cột 2 | Cột 3 |"
    col_divider = "| :---: | :---: | :---: | :---: |"
    table_rows.append(col_headers)
    table_rows.append(col_divider)

    for r in range(3):
        row_cells = [f"**Hàng {r+1}**"]
        for c in range(3):
            val = b[r][c]
            if val == "X":
                row_cells.append("&nbsp;&nbsp;❌&nbsp;&nbsp;")
            elif val == "O":
                row_cells.append("&nbsp;&nbsp;⭕&nbsp;&nbsp;")
            else:
                if game_over:
                    row_cells.append("&nbsp;&nbsp;⬜&nbsp;&nbsp;")
                else:
                    issue_link = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/issues/new?title=ttt%7C{r}%7C{c}&body=Click+%27Submit+new+issue%27+without+changing+anything+to+make+this+move!"
                    row_cells.append(f"&nbsp;&nbsp;[&nbsp;⬜&nbsp;]({issue_link})&nbsp;&nbsp;")
        table_rows.append("| " + " | ".join(row_cells) + " |")

    board_md = "\n".join(table_rows)

    reset_link = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/issues/new?title=ttt%7Creset&body=Click+%27Submit+new+issue%27+to+start+a+new+game!"
    
    score = state.get("score", {"X": 0, "O": 0, "Ties": 0})
    score_text = f"🏆 **Tỉ số:** Người chơi (❌) `{score['X']}` — `{score['O']}` Jhanh Bot (⭕) *(Hòa: `{score['Ties']}`)*"

    res = []
    res.append(f"<!-- TIC-TAC-TOE-STATE: {json.dumps(state)} -->")
    res.append("<div align=\"center\">")
    res.append("")
    res.append("### 🎮 Cờ Caro (Tic-Tac-Toe) vs Jhanh Bot")
    res.append(f"> {state['status']}")
    res.append("")
    res.append(board_md)
    res.append("")
    res.append(f"{score_text}")
    res.append("")
    res.append(f"👉 **[🔄 Bắt đầu ván mới (Reset Game)]({reset_link})**")
    res.append("")
    res.append("<sub><i>(Mẹo: Nhấn vào ô trống ⬜ hoặc Reset ➔ Bấm <b>Submit new issue</b> để đi nước cờ)</i></sub>")
    res.append("")
    res.append("</div>")

    return "\n".join(res)

def play(title, user):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Find existing state
    state_match = re.search(r'<!-- TIC-TAC-TOE-STATE: (.*?) -->', content)
    if state_match:
        try:
            state = json.loads(state_match.group(1))
        except Exception:
            state = None
    else:
        state = None

    if not state:
        state = {
            "board": [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]],
            "status": "Đến lượt bạn (**❌**)! Nhấn vào một ô trống ⬜ bên dưới để đánh.",
            "score": {"X": 0, "O": 0, "Ties": 0}
        }

    parts = title.strip().split("|")
    cmd = parts[1] if len(parts) > 1 else ""

    if cmd == "reset":
        state["board"] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        state["status"] = f"🎮 Ván mới đã được tạo bởi @{user}! Đến lượt bạn (**❌**)."
    elif len(parts) >= 3:
        try:
            r = int(parts[1])
            c = int(parts[2])
        except ValueError:
            return

        if 0 <= r <= 2 and 0 <= c <= 2:
            b = state["board"]
            # If current game already finished, auto-reset first
            if check_winner(b) or is_full(b):
                b = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                state["board"] = b

            if b[r][c] == " ":
                # Player move
                b[r][c] = "X"
                winner = check_winner(b)
                if winner == "X":
                    state["status"] = f"🎉 Chúc mừng @{user} (**❌**) đã chiến thắng!"
                    state["score"]["X"] = state["score"].get("X", 0) + 1
                elif is_full(b):
                    state["status"] = f"🤝 Ván cờ hòa (Draw)! Một trận đấu cân sức từ @{user}."
                    state["score"]["Ties"] = state["score"].get("Ties", 0) + 1
                else:
                    # AI move
                    ai_move = find_best_ai_move(b)
                    if ai_move:
                        b[ai_move[0]][ai_move[1]] = "O"
                        ai_winner = check_winner(b)
                        if ai_winner == "O":
                            state["status"] = f"🤖 Bot (**⭕**) vừa đánh vào hàng {ai_move[0]+1}, cột {ai_move[1]+1} và giành chiến thắng!"
                            state["score"]["O"] = state["score"].get("O", 0) + 1
                        elif is_full(b):
                            state["status"] = f"🤝 Ván cờ hòa (Draw)!"
                            state["score"]["Ties"] = state["score"].get("Ties", 0) + 1
                        else:
                            state["status"] = f"Bot (**⭕**) đã đánh ô ({ai_move[0]+1}, {ai_move[1]+1}). Đến lượt bạn (**❌**)!"

    new_section = render_board(state)
    replacement = f"<!-- TIC-TAC-TOE:START -->\n{new_section}\n<!-- TIC-TAC-TOE:END -->"

    # Replace safely without regex escaping issues
    start_tag = "<!-- TIC-TAC-TOE:START -->"
    end_tag = "<!-- TIC-TAC-TOE:END -->"

    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag)
        end_idx = content.find(end_tag) + len(end_tag)
        updated_content = content[:start_idx] + replacement + content[end_idx:]
    else:
        footer_marker = "<!-- =========================================\n     🌊 FOOTER WAVE 🌊"
        if footer_marker in content:
            updated_content = content.replace(footer_marker, f"{replacement}\n\n{footer_marker}")
        else:
            updated_content = content + "\n\n" + replacement

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        play(sys.argv[1], sys.argv[2])
    else:
        play("ttt|reset", "Jhanh")

