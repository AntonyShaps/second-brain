import type { Entry } from "./types";

const API_URL =
    import.meta.env.VITE_API_URL ?? "http://127.0.0.1:8000";

export async function fetchEntries(
    signal?: AbortSignal,
): Promise<Entry[]> {
    const response = await fetch(`${API_URL}/entries`, {
        method: "GET",
        signal,
    });

    if (!response.ok) {
        throw new Error(
            `Could not load entries: ${response.status} ${response.statusText}`,
        );
    }
    return (await response.json()) as Entry[];
}
