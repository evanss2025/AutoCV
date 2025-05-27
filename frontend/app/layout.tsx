import type { Metadata } from "next";
import { Poppins } from "next/font/google";
import "./globals.css";

const poppins = Poppins({
  weight: '300',
  subsets: ["latin"],
})

export const metadata: Metadata = {
  title: "AutoCV",
  description: "Takes in someone's LinkedIn profile and creates a resume/CV for them!",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
        <body className={`justify-center items-center flex ${poppins.className}`}>
        {children}
      </body>
    </html>
  );
}
