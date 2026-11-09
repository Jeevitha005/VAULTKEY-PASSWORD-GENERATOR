import { useState } from "react";
import MainLayout from "./layouts/MainLayout";
import GeneratorPage from "./pages/GeneratorPage";
import HistoryPage from "./pages/HistoryPage";
import useTheme from "./hooks/useTheme";

export default function App() {
  const [activeTab, setActiveTab] = useState("generator");
  const { theme, toggleTheme } = useTheme();

  return (
    <MainLayout activeTab={activeTab} onTabChange={setActiveTab} theme={theme} onToggleTheme={toggleTheme}>
      {activeTab === "generator" ? <GeneratorPage /> : <HistoryPage />}
    </MainLayout>
  );
}
