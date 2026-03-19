< !DOCTYPE html >
    <html lang="en">
        <head>
            <meta charset="UTF-8">
                <title>AI Sales Pitch Coach</title>
                <script src="https://cdn.tailwindcss.com"></script>
        </head>

        <body class="bg-gradient-to-br from-purple-100 via-white to-pink-100 min-h-screen">

            <div class="flex">

                <!-- Sidebar -->
                <aside class="w-64 bg-white/40 backdrop-blur-lg p-6 shadow-lg">
                    <h1 class="text-purple-600 font-bold text-xl mb-6">PitchCoach</h1>
                    <nav class="space-y-4 text-gray-600">
                        <p class="text-purple-600 font-medium">Pitch Analysis</p>
                        <p>Insights</p>
                        <p>Transcription</p>
                        <p>Coaching</p>
                        <p>Scoring</p>
                    </nav>
                </aside>

                <!-- Main -->
                <main class="flex-1 p-10">
                    <div class="max-w-7xl mx-auto grid grid-cols-3 gap-8">

                        <!-- LEFT CONTENT -->
                        <div class="col-span-2">

                            <!-- Heading -->
                            <h2 class="text-4xl font-bold mb-2">Analyze your pitch</h2>
                            <p class="text-gray-500 mb-6">
                                Drop an audio file of a pitch or hit <span class="text-purple-600 underline">browse</span> to upload.
                            </p>

                            <!-- Upload -->
                            <div class="border-2 border-dashed border-purple-300 rounded-2xl p-12 text-center bg-white/50 backdrop-blur-lg shadow">
                                <p class="text-gray-500 text-lg">Drag & drop audio file or <span class="text-purple-600">Browse</span></p>
                                <p class="text-sm text-gray-400 mt-2">MP3, WAV, M4A • Max 30 min</p>
                            </div>

                            <!-- Button -->
                            <button class="mt-6 w-full py-4 rounded-2xl text-white font-semibold text-lg bg-gradient-to-r from-purple-500 to-pink-500 shadow-lg hover:scale-[1.02] transition">
                                Analyze My Pitch →
                            </button>

                            <!-- Features -->
                            <div class="grid grid-cols-2 gap-6 mt-10">

                                <div class="flex gap-4 bg-white/60 p-5 rounded-2xl shadow">
                                    <div class="text-3xl">🧠</div>
                                    <div>
                                        <h3 class="font-semibold text-lg">Psychological Insight</h3>
                                        <p class="text-gray-500 text-sm">Analyze emotional appeal & improvement areas</p>
                                    </div>
                                </div>

                                <div class="flex gap-4 bg-white/60 p-5 rounded-2xl shadow">
                                    <div class="text-3xl">📄</div>
                                    <div>
                                        <h3 class="font-semibold text-lg">Speech Transcription</h3>
                                        <p class="text-gray-500 text-sm">Full transcript with highlights</p>
                                    </div>
                                </div>

                            </div>

                        </div>

                        <!-- RIGHT PANEL -->
                        <div class="bg-white/60 backdrop-blur-xl rounded-3xl p-6 shadow-xl">

                            <!-- Score -->
                            <div class="flex items-center gap-4">
                                <div class="w-16 h-16 rounded-full bg-gradient-to-r from-purple-500 to-pink-500 flex items-center justify-center text-white text-xl font-bold">
                                    82
                                </div>
                                <div>
                                    <h3 class="font-semibold">Analyze</h3>
                                    <p class="text-gray-500 text-sm">Your pitch metrics</p>
                                </div>
                            </div>

                            <!-- Bars -->
                            <div class="mt-6 space-y-4">

                                <div>
                                    <p class="text-sm">Persuasion</p>
                                    <div class="h-2 bg-gray-200 rounded">
                                        <div class="h-2 bg-purple-500 w-2/3 rounded"></div>
                                    </div>
                                </div>

                                <div>
                                    <p class="text-sm">Structure</p>
                                    <div class="h-2 bg-gray-200 rounded">
                                        <div class="h-2 bg-blue-400 w-1/2 rounded"></div>
                                    </div>
                                </div>

                                <div>
                                    <p class="text-sm">Confidence</p>
                                    <div class="h-2 bg-gray-200 rounded">
                                        <div class="h-2 bg-pink-400 w-2/3 rounded"></div>
                                    </div>
                                </div>

                                <div>
                                    <p class="text-sm">Clarity</p>
                                    <div class="h-2 bg-gray-200 rounded">
                                        <div class="h-2 bg-green-400 w-3/4 rounded"></div>
                                    </div>
                                </div>

                            </div>

                            <!-- Remarks -->
                            <div class="mt-6 bg-white p-4 rounded-xl shadow">
                                <h4 class="font-semibold mb-2">Remarks:</h4>
                                <p class="text-gray-500 text-sm">
                                    Great start! Engage prospects by asking questions. Explain benefits with vivid examples. End with a strong CTA.
                                </p>
                            </div>

                        </div>

                    </div>

                    <!-- Bottom Section -->
                    <div class="max-w-7xl mx-auto mt-16">

                        <h2 class="text-3xl font-bold text-center mb-8">
                            Boost your sales pitch performance
                        </h2>

                        <div class="grid grid-cols-4 gap-6">

                            <div class="bg-white/60 p-6 rounded-2xl shadow text-center">
                                <h3 class="font-semibold">Psychological Insight Analysis</h3>
                            </div>

                            <div class="bg-white/60 p-6 rounded-2xl shadow text-center">
                                <h3 class="font-semibold">Personalized Transcription</h3>
                            </div>

                            <div class="bg-white/60 p-6 rounded-2xl shadow text-center">
                                <h3 class="font-semibold">Actionable Coaching</h3>
                            </div>

                            <div class="bg-white/60 p-6 rounded-2xl shadow text-center">
                                <h3 class="font-semibold">Performance Strategy</h3>
                            </div>

                        </div>

                    </div>

                </main>

            </div>

        </body>
    </html>