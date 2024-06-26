"use client";

import { GoogleOAuthProvider } from "@react-oauth/google";
import React from "react";
import { QueryClient, QueryClientProvider } from "react-query";

export const queryClient = new QueryClient();
export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <GoogleOAuthProvider clientId={process.env.NEXT_PUBLIC_GOOGLE_ID as string}>
      <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
    </GoogleOAuthProvider>
  );
}
