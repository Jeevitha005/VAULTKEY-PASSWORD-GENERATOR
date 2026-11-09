import { FiDownload, FiFileText, FiTrash2 } from "react-icons/fi";
import HistoryItem from "./HistoryItem";
import Loader from "./Loader";
import { downloadFromUrl, downloadJson } from "../utils/download";
import { getExportCsvUrl, getExportTxtUrl } from "../services/passwordService";

export default function HistoryList({ entries, isLoading, onClear }) {
  function handleDownloadJson() {
    downloadJson(entries, "password-history.json");
  }

  return (
    <div className="glass-panel flex flex-col gap-4 p-5 sm:p-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <h2 className="font-display text-sm font-semibold uppercase tracking-wide text-vault-950/60 dark:text-slate-400">
          Recent passwords
        </h2>

        <div className="flex flex-wrap gap-2">
          <button type="button" onClick={() => downloadFromUrl(getExportTxtUrl())} className="btn-secondary text-xs">
            <FiFileText /> TXT
          </button>
          <button type="button" onClick={() => downloadFromUrl(getExportCsvUrl())} className="btn-secondary text-xs">
            <FiFileText /> CSV
          </button>
          <button type="button" onClick={handleDownloadJson} className="btn-secondary text-xs">
            <FiDownload /> Download
          </button>
          <button
            type="button"
            onClick={onClear}
            className="btn-secondary text-xs text-strength-weak hover:bg-strength-weak/10"
          >
            <FiTrash2 /> Clear
          </button>
        </div>
      </div>

      {isLoading ? (
        <Loader label="Loading history" />
      ) : entries.length === 0 ? (
        <p className="py-8 text-center text-sm text-vault-950/40 dark:text-slate-500">
          No passwords generated yet. Head to the Generator tab to create one.
        </p>
      ) : (
        <div className="flex flex-col divide-y divide-vault-950/5 dark:divide-white/5">
          {entries.map((entry) => (
            <HistoryItem key={entry.id} entry={entry} />
          ))}
        </div>
      )}
    </div>
  );
}
