import { useEffect, useState } from "react";

import { fetchEntries } from "./api";
import type { Entry } from "./types";

export function EntryList() {
    const [entries, setEntries] = useState<Entry[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const controller = new AbortController();

        async function loadEntries() {
            try {
                const loadedEntries = await fetchEntries(controller.signal);
                setEntries(loadedEntries);
            } catch (error: unknown) {
                if (controller.signal.aborted) {
                    return;
                }
                const message =
                    error instanceof Error
                        ? error.message
                        : "An unexpected error occurred";
                setError(message);
            } finally {
                if (!controller.signal.aborted) {
                    setIsLoading(false);
                }
            }
        }

        void loadEntries();

        return () => {
            controller.abort();
        };
    }, []);

    if (isLoading) {
        return <p> Loading etries...</p>;
    }

    if (error !==null) {
        return <p role="alert">{error}</p>;
    }

    if (entries.length === 0) {
        return <p> No entries yet.</p>;
    }

    return (
        <section>
        <h2>Entries</h2>
        <ul>
        {entries.map((entry) => (
            <li key={entry.id}>
              <h3>{entry.title}</h3>

              <p>
                <strong> Type: </strong> {entry.type}
              </p>

              {entry.contents !== null && (
                  <p>{entry.contents}</p>
              )}

              {entry.tags.length > 0 && (
                  <p>
                  <strong>Tags:</strong> {entry.tags.join(", ")}
                  </p>
              )}
              </li>
        ))}
        </ul>
        </section>
    );
}
            











