import { useCallback, useEffect, useState } from "react";
import toast from "react-hot-toast";
import HistoryList from "../components/HistoryList";
import { clearHistory, fetchHistory } from "../services/passwordService";

export default function HistoryPage() {
  const [entries, setEntries] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const loadHistory = useCallback(async () => {
    setIsLoading(true);
    try {
      const data = await fetchHistory();
      setEntries(data);
    } catch (error) {
      toast.error(error.message || "Failed to load history.");
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    loadHistory();
  }, [loadHistory]);

  async function handleClear() {
    try {
      await clearHistory();
      setEntries([]);
      toast.success("History cleared");
    } catch (error) {
      toast.error(error.message || "Failed to clear history.");
    }
  }

  return (
    <div className="flex flex-col gap-6">
      <div>
        <h1 className="font-display text-2xl font-bold sm:text-3xl">Password history</h1>
        <p className="mt-1 text-sm text-vault-950/50 dark:text-slate-400">
          Every password you generate is saved here so you can copy or export it later.
        </p>
      </div>

      <HistoryList entries={entries} isLoading={isLoading} onClear={handleClear} />
    </div>
  );
}
