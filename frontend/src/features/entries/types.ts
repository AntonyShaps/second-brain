export type EntryType = "note" | "task" | "project";

export interface {
    id: string;
    type: EntryType;
    title: string;
    contents: string | null;
    tags: string[];
}
