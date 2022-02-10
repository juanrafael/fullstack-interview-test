CREATE TABLE IF NOT EXISTS authors
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

\echo "Tabla authors creada"

CREATE TABLE IF NOT EXISTS pull_requests
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    author_id INT NOT NULL,
    source_branch VARCHAR(250) NOT NULL,
    target_branch VARCHAR(250) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES authors(id)
);

\echo "Tabla pull_requests creada"