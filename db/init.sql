CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE receipts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    status TEXT NOT NULL DEFAULT 'pending',
    s3_key TEXT,
    uploaded_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    extracted_data JSONB,
    error_message TEXT
);
