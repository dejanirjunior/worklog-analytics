CREATE TABLE IF NOT EXISTS worklogs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_date TEXT NOT NULL,
    developer_name TEXT NOT NULL,
    card_id TEXT,
    card_name TEXT NOT NULL,
    estimated_flag INTEGER DEFAULT 1,
    hours REAL NOT NULL,
    activity_type TEXT NOT NULL,
    comment TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS daily_plan (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    daily_date TEXT NOT NULL,
    developer_name TEXT NOT NULL,
    notes TEXT,
    absence_type TEXT,
    absence_detail TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS daily_plan_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    daily_plan_id INTEGER NOT NULL,
    card_id TEXT,
    card_name TEXT,
    client_name TEXT,
    source_type TEXT,
    is_selected INTEGER DEFAULT 1,
    blocker_text TEXT,
    trello_has_block_label INTEGER DEFAULT 0,
    needs_block_label_mark INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
