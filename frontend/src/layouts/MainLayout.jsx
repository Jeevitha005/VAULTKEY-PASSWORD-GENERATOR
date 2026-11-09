import { Toaster } from "react-hot-toast";
import Navbar from "../components/Navbar";
import Footer from "../components/Footer";

export default function MainLayout({ activeTab, onTabChange, theme, onToggleTheme, children }) {
  return (
    <div className="min-h-screen bg-vault-gradient dark:bg-vault-gradient bg-white dark:bg-vault-950">
      <Toaster
        position="top-center"
        toastOptions={{
          className: "font-body text-sm",
          style: { borderRadius: "12px" },
        }}
      />
      <Navbar activeTab={activeTab} onTabChange={onTabChange} theme={theme} onToggleTheme={onToggleTheme} />
      <main className="mx-auto max-w-3xl px-6 py-10">{children}</main>
      <Footer />
    </div>
  );
}
