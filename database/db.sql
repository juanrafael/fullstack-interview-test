CREATE TABLE IF NOT EXISTS pull_requests
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    author VARCHAR(150) NOT NULL,
    source_branch VARCHAR(250) NOT NULL,
    target_branch VARCHAR(250) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

\echo "Tabla pull_requests creada";