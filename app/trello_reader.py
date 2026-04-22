from pathlib import Path
import pandas as pd

CSV_PATH = Path("/home/junior/trello-dashboard/data/cards_enriched.csv")


def _safe_str(value):
    if pd.isna(value):
        return ""
    return str(value).strip()


def _split_members(raw_value):
    raw = _safe_str(raw_value)
    if not raw:
        return []
    return [x.strip() for x in raw.split(",") if x.strip()]


def _has_estimate(row):
    effort_value = row.get("effort")
    story_point_value = row.get("story_point")

    if pd.notna(effort_value):
        try:
            return 1 if float(effort_value) > 0 else 0
        except Exception:
            pass

    if pd.notna(story_point_value):
        try:
            return 1 if float(story_point_value) > 0 else 0
        except Exception:
            pass

    return 0


def _has_block_label(row):
    is_block_value = row.get("is_block")
    if pd.notna(is_block_value):
        value_str = str(is_block_value).strip().lower()
        if value_str in ("true", "1", "yes"):
            return 1

    labels_value = _safe_str(row.get("labels"))
    if "block" in labels_value.lower():
        return 1

    return 0


def load_cards():
    if not CSV_PATH.exists():
        return []

    try:
        df = pd.read_csv(CSV_PATH, encoding="utf-8-sig")

        allowed_lists = ["Refinado", "Em dev", "Q.A.", "UAT", "Concluído"]
        if "lista" in df.columns:
            df = df[df["lista"].isin(allowed_lists)]

        sort_cols = [c for c in ["assigned_members", "cliente_label", "lista", "card_name"] if c in df.columns]
        if sort_cols:
            df = df.sort_values(sort_cols)

        cards = []

        for _, row in df.iterrows():
            card_id = _safe_str(row.get("card_id"))
            card_name = _safe_str(row.get("card_name"))
            client_name = _safe_str(row.get("cliente_label"))
            lista = _safe_str(row.get("lista"))
            assigned_members = _split_members(row.get("assigned_members"))
            estimated_flag = _has_estimate(row)
            has_block_label = _has_block_label(row)

            if not card_name:
                continue

            cards.append({
                "card_id": card_id,
                "card_name": card_name,
                "client_name": client_name,
                "lista": lista,
                "assigned_members": assigned_members,
                "estimated_flag": estimated_flag,
                "has_block_label": has_block_label,
                "priority": _safe_str(row.get("priority")),
                "risk": _safe_str(row.get("risk")),
                "due_date": _safe_str(row.get("due_date")),
                "data_compromisso": _safe_str(row.get("data_compromisso")),
                "last_activity": _safe_str(row.get("last_activity")),
                "created_date": _safe_str(row.get("created_date")),
                "effort": _safe_str(row.get("effort")),
                "story_point": _safe_str(row.get("story_point"))
            })

        return cards

    except Exception as e:
        print(f"Erro ao ler cards do Trello: {e}")
        return []


