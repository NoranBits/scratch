import os
import json
import re
import subprocess
from pathlib import Path

def get_github_url():
    try:
        remotes = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True).stdout
        match = re.search(r'github\.com[:/](.+?)\.git', remotes)
        if match:
            return f"https://github.com/{match.group(1)}"
    except:
        pass
    return None

GITHUB_REPO_URL = get_github_url()

# --- TEMPLATES ---
ROOT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AntiGravity | Mission Control</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&display=swap');
        :root {{ --cyan: #22d3ee; --purple: #a855f7; --emerald: #10b981; --amber: #f59e0b; --rose: #f43f5e; --bg: #020617; }}
        body {{ background-color: var(--bg); color: #f8fafc; font-family: 'Outfit', sans-serif; overflow-x: hidden; }}
        .glass {{ background: rgba(15, 23, 42, 0.6); backdrop-filter: blur(24px); border: 1px solid rgba(255, 255, 255, 0.1); }}
        .cyber-grid {{ background-image: linear-gradient(rgba(34, 211, 238, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(34, 211, 238, 0.03) 1px, transparent 1px); background-size: 40px 40px; }}
        .neuron-node {{ stroke: #fff; stroke-width: 1px; cursor: pointer; transition: all 0.3s; opacity: 0.8; }}
        .neuron-node.active {{ stroke-width: 3px; filter: drop-shadow(0 0 12px var(--cyan)); opacity: 1; }}
        .neuron-node.dimmed {{ opacity: 0.2; }}
        .neuron-link {{ stroke: rgba(34, 211, 238, 0.1); stroke-opacity: 0.4; stroke-width: 1px; transition: all 0.3s; }}
        .neuron-link.active {{ stroke-opacity: 1; stroke-width: 2px; stroke: var(--cyan); }}
        .neuron-link.dimmed {{ stroke-opacity: 0.05; }}
        .pulse {{ animation: neural-pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite; }}
        @keyframes neural-pulse {{ 0%, 100% {{ opacity: 0.3; }} 50% {{ opacity: 0.8; }} }}
        #tooltip {{ position: absolute; pointer-events: none; padding: 12px; font-size: 11px; z-index: 100; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); opacity: 0; transition: opacity 0.2s; }}
    </style>
</head>
<body class="cyber-grid min-h-screen">
    <div id="tooltip" class="glass border-cyan-500/30"></div>
    <div class="relative z-10 p-8 max-w-7xl mx-auto space-y-8">
        <!-- Header -->
        <header class="flex justify-between items-center glass p-6 rounded-2xl border-cyan-500/20">
            <div class="flex items-center gap-6">
                <div class="w-16 h-16 bg-gradient-to-br from-cyan-400 to-purple-600 rounded-2xl flex items-center justify-center text-3xl font-black text-white italic shadow-[0_0_20px_rgba(34,211,238,0.4)]">AG</div>
                <div>
                    <h1 class="text-4xl font-extrabold tracking-tighter uppercase mb-1">Mission Control</h1>
                    <div class="flex items-center gap-3">
                        <p class="text-sm font-mono text-cyan-400/80 tracking-widest uppercase italic">Architectural Neuron Interface v4.5</p>
                        <script>
                            const GITHUB_REPO_URL = {GITHUB_REPO_URL};
                            if (GITHUB_REPO_URL) {
                                document.write(`
                                    <a href="${GITHUB_REPO_URL}" target="_blank" class="glass px-2 py-0.5 rounded text-[10px] text-slate-400 hover:text-cyan-400 border-white/5 flex items-center gap-1.5 transition-all">
                                        <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
                                        GitHub Repo
                                    </a>
                                `);
                            }
                        </script>
                    </div>
                </div>
            </div>
            <div class="text-right hidden md:block space-y-2">
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-[0.3em] mb-1">Current Protocol</div>
                <div class="flex flex-col items-end gap-2">
                    <div class="text-xs font-mono text-emerald-400 bg-emerald-500/10 px-3 py-1 rounded-full border border-emerald-500/20">NEURAL_INSIGHTS_ENGAGED</div>
                    <script>
                        if (GITHUB_REPO_URL) {
                            document.write(`
                                <img src="${GITHUB_REPO_URL}/actions/workflows/ag_ecosystem_release.yml/badge.svg" alt="CI Status" class="h-4 opacity-80 hover:opacity-100 transition-opacity">
                            `);
                        }
                    </script>
                </div>
            </div>
        </header>

        <div class="grid lg:grid-cols-[1fr_400px] gap-8">
            <div class="space-y-8">
                <!-- Neural Network Visualization -->
                <section class="glass rounded-3xl border-slate-700/50 overflow-hidden relative min-h-[550px]">
                    <div class="absolute top-6 left-6 z-20">
                        <h2 class="text-xs font-bold text-cyan-400 uppercase tracking-widest mb-1">Architectural Neuron Graph</h2>
                        <p class="text-[10px] text-slate-500 italic">Hover to focus associations. Click to navigate.</p>
                    </div>
                    <!-- Legend -->
                    <div class="absolute bottom-6 right-6 z-20 glass p-3 rounded-xl border-white/5 space-y-2 text-[9px] font-bold uppercase tracking-widest">
                        <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-cyan-400"></span> <span>Root Node</span></div>
                        <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-purple-500"></span> <span>Python Tool</span></div>
                        <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> <span>Node Tool</span></div>
                        <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-amber-500"></span> <span>Sample</span></div>
                        <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-rose-500"></span> <span>Data Layer</span></div>
                        <div class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-blue-500"></span> <span>Remote Repo</span></div>
                    </div>
                    <div id="neuron-graph" class="w-full h-[550px]"></div>
                </section>

                <!-- Knowledge Base & Governance -->
                <div class="grid md:grid-cols-2 gap-8">
                    <section class="glass p-8 rounded-2xl border-cyan-500/20 space-y-6">
                        <div class="flex items-center gap-4">
                            <div class="p-3 bg-cyan-500/10 rounded-xl"><svg class="w-6 h-6 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg></div>
                            <h2 class="text-2xl font-bold tracking-tighter uppercase">Knowledge Base</h2>
                        </div>
                        <ul class="space-y-3">
                            <li><a href=".ai/INDEX.md" class="text-sm text-slate-400 hover:text-cyan-400 flex justify-between group transition-all"><span>System Index</span><span class="text-[10px] opacity-0 group-hover:opacity-100 italic transition-all">View INDEX.md &rarr;</span></a></li>
                            <li><a href=".ai/STATE/readme.html" class="text-sm text-slate-400 hover:text-cyan-400 flex justify-between group transition-all"><span>State Anchors</span><span class="text-[10px] opacity-0 group-hover:opacity-100 italic transition-all">View State &rarr;</span></a></li>
                            <li><a href=".ai/SKILLS/INDEX.md" class="text-sm text-slate-400 hover:text-cyan-400 flex justify-between group transition-all"><span>Skill Registry</span><span class="text-[10px] opacity-0 group-hover:opacity-100 italic transition-all">View Skills &rarr;</span></a></li>
                        </ul>
                    </section>
                    <section class="glass p-8 rounded-2xl border-purple-500/20 space-y-6">
                        <div class="flex items-center gap-4">
                            <div class="p-3 bg-purple-500/10 rounded-xl"><svg class="w-6 h-6 text-purple-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg></div>
                            <h2 class="text-2xl font-bold tracking-tighter uppercase">Governance</h2>
                        </div>
                        <ul class="space-y-3">
                            <li><a href=".ai/tools/HARMONIZATION_RULES.json" class="text-sm text-slate-400 hover:text-purple-400 flex justify-between group transition-all"><span>Harmonization Rules</span><span class="text-[10px] opacity-0 group-hover:opacity-100 italic transition-all">View JSON &rarr;</span></a></li>
                            <li><a href=".ai/DECISIONS/readme.html" class="text-sm text-slate-400 hover:text-purple-400 flex justify-between group transition-all"><span>Architectural Decisions</span><span class="text-[10px] opacity-0 group-hover:opacity-100 italic transition-all">View ADRs &rarr;</span></a></li>
                        </ul>
                    </section>
                </div>
            </div>

            <aside class="space-y-8">
                <!-- System Stats (Live) -->
                <section class="glass p-8 rounded-2xl border-emerald-500/20 space-y-8">
                    <h3 class="text-xs font-bold text-emerald-400 uppercase tracking-widest">Architectural Health</h3>
                    <div class="space-y-6">
                        <div class="space-y-2">
                            <div class="flex justify-between text-[10px] font-mono text-slate-500 uppercase tracking-widest"><span>Token Efficiency</span><span id="stat-eff" class="text-white">--%</span></div>
                            <div class="h-1.5 bg-slate-800 rounded-full overflow-hidden"><div id="bar-eff" class="bg-gradient-to-r from-emerald-500 to-cyan-500 h-full w-0 transition-all duration-1000"></div></div>
                        </div>
                        <div class="space-y-2">
                            <div class="flex justify-between text-[10px] font-mono text-slate-500 uppercase tracking-widest"><span>System Volume</span><span id="stat-vol" class="text-white">-- KB</span></div>
                            <div class="h-1.5 bg-slate-800 rounded-full overflow-hidden"><div id="bar-vol" class="bg-gradient-to-r from-purple-500 to-pink-500 h-full w-[60%] transition-all duration-1000"></div></div>
                        </div>
                        <div class="grid grid-cols-2 gap-4">
                            <div class="p-4 bg-slate-900/40 rounded-xl border border-white/5">
                                <span class="block text-[10px] text-slate-500 uppercase mb-1">Git Branch</span>
                                <span id="git-branch" class="text-xs font-bold font-mono text-cyan-400 tracking-widest text-ellipsis overflow-hidden">--</span>
                            </div>
                            <div class="p-4 bg-slate-900/40 rounded-xl border border-white/5">
                                <span class="block text-[10px] text-slate-500 uppercase mb-1">Git Pulse</span>
                                <span id="git-status" class="text-xs font-bold font-mono text-purple-400 tracking-widest text-ellipsis overflow-hidden">--</span>
                            </div>
                        </div>
                        <div class="grid grid-cols-2 gap-4">
                            <div class="p-4 bg-slate-900/40 rounded-xl border border-white/5">
                                <span class="block text-[10px] text-slate-500 uppercase mb-1">Shared Deps</span>
                                <span id="dep-shared" class="text-xs font-bold font-mono text-emerald-400 tracking-widest">--</span>
                            </div>
                            <div class="p-4 bg-slate-900/40 rounded-xl border border-white/5">
                                <span class="block text-[10px] text-slate-500 uppercase mb-1">Conflicts</span>
                                <span id="dep-conflicts" class="text-xs font-bold font-mono text-rose-400 tracking-widest">--</span>
                            </div>
                        </div>

                        <div class="pt-4 border-t border-white/5 mt-4">
                            <h3 class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3">Commit Security</h3>
                            <div class="p-4 bg-slate-950/80 rounded-xl border border-emerald-500/20 flex items-center gap-3">
                                <div id="gpg-status-icon" class="w-2 h-2 rounded-full bg-slate-700 animate-pulse"></div>
                                <div>
                                    <span id="gpg-status-text" class="block text-[10px] font-bold text-slate-500 uppercase tracking-tighter">Initializing...</span>
                                    <code id="gpg-fingerprint" class="text-[9px] font-mono text-slate-500">Unprovisioned</code>
                                </div>
                            </div>
                        </div>

                        <div class="pt-4 border-t border-white/5 mt-4">
                            <h3 class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3" onclick="copyToClipboard('npm run bash')">Terminal Hub</h3>
                            <div class="p-4 bg-slate-950/80 rounded-xl border border-cyan-500/20 group hover:border-cyan-500/40 transition-all cursor-pointer">
                                <div class="flex justify-between items-center mb-1">
                                    <span class="text-[9px] font-bold text-cyan-400 uppercase tracking-tighter">GIT BASH</span>
                                    <span class="text-[8px] text-slate-600 font-mono group-hover:text-cyan-400 transition-colors">Click to Copy</span>
                                </div>
                                <code class="text-[11px] font-mono text-slate-300">npm run bash</code>
                            </div>
                        </div>

                        <!-- Release Radar -->
                        <div class="pt-4 border-t border-white/5 mt-4">
                            <h3 class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3">Release Radar</h3>
                            <div id="release-radar" class="space-y-3">
                                <!-- Populated by JS -->
                            </div>
                        </div>
                    </div>
                </section>
            </aside>
        </div>
    </div>

    <script>
        const colorMap = {{
            "root": "#22d3ee",
            "tool_py": "#a855f7",
            "tool_node": "#10b981",
            "sample": "#f59e0b",
            "data": "#f43f5e",
            "remote_repo": "#3b82f6",
            "directory": "#64748b"
        }};

        async function init() {{
            const stats = {stats_json};
            const graph = {graph_json};
            const currentPath = "{rel_path_val}";
            
            // Stats Update
            document.getElementById('stat-eff').innerText = stats.avg_efficiency + '%';
            document.getElementById('bar-eff').style.width = stats.avg_efficiency + '%';
            document.getElementById('stat-vol').innerText = (stats.total_volume_bytes / 1024).toFixed(1) + ' KB';

            if (stats.git_pulse) {{
                document.getElementById('git-branch').innerText = stats.git_pulse.branch;
                document.getElementById('git-status').innerText = stats.git_pulse.status;
            }}
            
            if (stats.git_pulse && stats.git_pulse.phases) {{
                const radar = document.getElementById('release-radar');
                const phases = ["dev", "demos", "alphas", "betas", "open-betas", "production", "maintenance"];
                radar.innerHTML = phases.map(p => {{
                    const data = stats.git_pulse.phases[p];
                    const exists = data && data.exists;
                    const isActive = stats.git_pulse.branch === p;
                    return `
                        <div class="flex items-center gap-3 p-2 bg-slate-950/40 rounded-lg border border-white/5 ${{isActive ? 'border-cyan-500/30 bg-cyan-500/5' : ''}}">
                            <div class="w-1.5 h-1.5 rounded-full ${{exists ? 'bg-cyan-400' : 'bg-slate-700'}}"></div>
                            <div class="flex-grow">
                                <div class="text-[9px] font-bold ${{isActive ? 'text-cyan-400' : 'text-slate-400'}} uppercase">${{p}}</div>
                                <div class="text-[8px] font-mono text-slate-600">${{exists ? data.last_commit : 'NOT PROVISIONED'}}</div>
                            </div>
                            ${{isActive ? '<span class="text-[7px] bg-cyan-500/20 text-cyan-400 px-1 rounded">ACTIVE</span>' : ''}}
                        </div>
                    `;
                }}).join('');
            }}

            const container = document.getElementById('neuron-graph');
            let width = container.clientWidth;
            let height = container.clientHeight;

            const svg = d3.select("#neuron-graph").append("svg")
                .attr("viewBox", [0, 0, width, height]);

            const simulation = d3.forceSimulation(graph.nodes)
                .force("link", d3.forceLink(graph.links).id(d => d.id).distance(100))
                .force("charge", d3.forceManyBody().strength(-300))
                .force("center", d3.forceCenter(width / 2, height / 2));

            const link = svg.append("g")
                .selectAll("line")
                .data(graph.links)
                .join("line")
                .attr("class", "neuron-link");

            const node = svg.append("g")
                .selectAll("circle")
                .data(graph.nodes)
                .join("circle")
                .attr("r", d => d.type === "root" ? 12 : 8)
                .attr("class", "neuron-node")
                .attr("fill", d => colorMap[d.type])
                .call(d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended))
                .on("mouseover", (e, d) => {{
                    // Tooltip
                    const tooltip = d3.select("#tooltip");
                    tooltip.style("opacity", 1)
                        .html(`<div class="font-bold text-cyan-400 mb-1">${{d.name}}</div>
                               <div class="text-[10px] text-slate-400 mb-2">${{d.path}}</div>
                               <div class="flex justify-between border-t border-white/5 pt-2">
                                <span>Volume:</span> <span class="text-white">${{(d.size_raw / 1024).toFixed(1)}} KB</span>
                               </div>
                               <div class="flex justify-between">
                                <span>Efficiency:</span> <span class="text-white">${{d.eff}}%</span>
                               </div>`)
                        .style("left", (e.pageX + 15) + "px")
                        .style("top", (e.pageY - 15) + "px");

                    // Highlight neighbors
                    const neighbors = new Set();
                    graph.links.forEach(l => {{
                        if (l.source.id === d.id) neighbors.add(l.target.id);
                        if (l.target.id === d.id) neighbors.add(l.source.id);
                    }});

                    node.classed("dimmed", n => n.id !== d.id && !neighbors.has(n.id));
                    link.classed("active", l => l.source.id === d.id || l.target.id === d.id);
                    link.classed("dimmed", l => l.source.id !== d.id && l.target.id !== d.id);
                    d3.select(e.currentTarget).classed("active", true).attr("r", d.type === "root" ? 15 : 10);
                }})
                .on("mousemove", (e) => {{
                    d3.select("#tooltip")
                        .style("left", (e.pageX + 15) + "px")
                        .style("top", (e.pageY - 15) + "px");
                }})
                .on("mouseout", (e, d) => {{
                    d3.select("#tooltip").style("opacity", 0);
                    node.classed("dimmed", false);
                    link.classed("active", false);
                    link.classed("dimmed", false);
                    d3.select(e.currentTarget).classed("active", false).attr("r", d.type === "root" ? 12 : 8);
                }})
                .on("click", (e, d) => window.location.href = (currentPath === "." ? "" : "../".repeat(currentPath.split('/').length)) + d.path + '/readme.html');

            simulation.on("tick", () => {{
                link.attr("x1", d => d.source.x).attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
                node.attr("cx", d => d.x).attr("cy", d => d.y);
            }});

            function dragstarted(event) {{
                if (!event.active) simulation.alphaTarget(0.3).restart();
                event.subject.fx = event.subject.x;
                event.subject.fy = event.subject.y;
            }}
            function dragged(event) {{
                event.subject.fx = event.x;
                event.subject.fy = event.y;
            }}
            function dragended(event) {{
                if (!event.active) simulation.alphaTarget(0);
                event.subject.fx = null;
                event.subject.fy = null;
            }}
        }}
        init();
    </script>
</body>
</html>
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AntiGravity | {title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=JetBrains+Mono:wght@400;700&display=swap');
        :root {{ --cyan: #22d3ee; --purple: #a855f7; --bg: #020617; }}
        body {{ background-color: var(--bg); color: #f8fafc; font-family: 'Outfit', sans-serif; min-height: 100vh; }}
        .glass {{ background: rgba(15, 23, 42, 0.4); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }}
        .cyber-grid {{ background-image: linear-gradient(rgba(34, 211, 238, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(34, 211, 238, 0.03) 1px, transparent 1px); background-size: 40px 40px; }}
        .neuron-node {{ stroke: #fff; stroke-width: 1px; cursor: pointer; opacity: 0.8; }}
        .neuron-node.active {{ stroke-width: 2px; filter: drop-shadow(0 0 8px var(--cyan)); opacity: 1; }}
        .neuron-link {{ stroke: rgba(34, 211, 238, 0.1); stroke-opacity: 0.4; stroke-width: 1px; }}
        .file-row:hover {{ background: rgba(255, 255, 255, 0.03); }}
    </style>
</head>
<body class="bg-slate-950 text-slate-200 font-sans min-h-screen flex flex-col items-center">
    <!-- Neural Header (Sticky & Responsive) -->
    <section class="sticky top-0 z-50 w-full glass border-b border-white/10 overflow-hidden min-h-[300px] shadow-2xl backdrop-blur-xl">
        <div class="absolute top-4 left-6 z-20 pointer-events-none">
            <h2 class="text-[10px] font-bold text-cyan-400 uppercase tracking-[0.3em] mb-1">Architectural Pulse</h2>
            <p class="text-[9px] text-slate-500 italic">Always-in-view neural context.</p>
        </div>
        <div id="neuron-graph" class="w-full h-[300px]"></div>
    </section>

    <div class="w-full max-w-6xl p-6 lg:p-12 space-y-8 relative z-10">
        <nav class="flex items-center justify-between glass p-4 rounded-xl">
            <div class="flex items-center gap-4">
                <div class="w-8 h-8 bg-gradient-to-br from-cyan-400 to-purple-600 rounded-lg flex items-center justify-center font-bold text-white italic">AG</div>
                <div class="flex flex-col">
                    <span class="text-xs font-bold text-slate-500 uppercase tracking-widest">Architectural Node</span>
                    <span class="text-sm font-mono text-cyan-400">{rel_path}</span>
                </div>
            </div>
            <div class="flex items-center gap-6">
                <a href="{parent_link}" class="text-xs font-bold text-slate-400 hover:text-white transition-all uppercase tracking-widest flex items-center gap-2">
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                    Back
                </a>
                {github_link}
            </div>
        </nav>

        <div class="grid lg:grid-cols-[1fr_350px] gap-8">
            <div class="space-y-8">
                <!-- Guidance & Plans -->
                <section class="grid md:grid-cols-2 gap-6">
                    <div class="glass p-6 rounded-2xl border-cyan-500/20">
                        <h3 class="text-xs font-bold text-cyan-400 uppercase tracking-widest mb-4">System Guidance</h3>
                        <div class="text-sm text-slate-300 leading-relaxed italic">
                            {guidance}
                        </div>
                    </div>
                    <div class="glass p-6 rounded-2xl border-purple-500/20">
                        <h3 class="text-xs font-bold text-purple-400 uppercase tracking-widest mb-4">Future Plans</h3>
                        <ul class="text-xs text-slate-400 space-y-2">
                            {plans}
                        </ul>
                    </div>
                </section>

                <!-- Contents -->
                <section class="glass rounded-2xl border-slate-700/50 overflow-hidden">
                    <div class="bg-slate-900/60 px-6 py-4 border-b border-slate-800/50 flex justify-between items-center">
                        <h2 class="text-xl font-bold text-white uppercase tracking-tighter">Node Contents</h2>
                        <span class="text-[10px] font-mono text-slate-500">{item_count} items detected</span>
                    </div>
                    <div class="divide-y divide-slate-800/40 max-h-[600px] overflow-y-auto scroll-hide">
                        {items}
                    </div>
                </section>
            </div>

            <!-- Stats Sidebar -->
            <aside class="space-y-8">
                <section class="glass p-6 rounded-2xl border-purple-500/20">
                    <h3 class="text-xs font-bold text-purple-400 uppercase tracking-widest mb-6">Volume & Density</h3>
                    <div class="aspect-square relative flex items-center justify-center">
                        <canvas id="typeChart"></canvas>
                        <div class="absolute text-center">
                            <span class="block text-2xl font-black text-white">{efficiency}%</span>
                            <span class="text-[10px] font-mono text-slate-500 uppercase tracking-widest">Token Efficiency</span>
                        </div>
                    </div>
                    <div class="mt-6 space-y-4">
                        <div class="flex justify-between text-[10px] font-mono text-slate-500 uppercase">
                            <span>Total Volume</span>
                            <span class="text-white">{total_size}</span>
                        </div>
                        <div class="h-1.5 bg-slate-800 rounded-full overflow-hidden">
                            <div class="bg-purple-500 h-full shadow-[0_0_8px_var(--purple)]" style="width: {efficiency}%"></div>
                        </div>
                        <div class="p-3 bg-slate-950/50 rounded-lg border border-slate-800/50">
                            <p class="text-[10px] text-slate-500 uppercase mb-1">Architecture Note</p>
                            <p class="text-[11px] text-slate-300 italic">"Token density relative to total bytes. Optimal threshold &gt;85%."</p>
                        </div>
                    </div>
                </section>
            </aside>
        </div>

        <footer class="text-center py-8">
            <p class="text-[10px] font-mono text-slate-600 tracking-widest uppercase italic">AntiGravity Navigation Protocol v3.0 | ARCH_NEURAL_STABLE</p>
        </footer>
    </div>

    <script>
        const ctx = document.getElementById('typeChart').getContext('2d');
        const stats = {stats_json};
        const graph = {graph_json};
        const currentPath = "{rel_path_val}";
        
        new Chart(ctx, {{
            type: 'doughnut',
            data: {{
                labels: Object.keys(stats),
                datasets: [{{
                    data: Object.values(stats),
                    backgroundColor: ['#22d3ee', '#a855f7', '#10b981', '#f59e0b', '#ef4444', '#6366f1'],
                    borderWidth: 0,
                    hoverOffset: 4
                }}]
            }},
            options: {{ cutout: '80%', plugins: {{ legend: {{ display: false }} }} }}
        }});

        // Neuron Pulse Header
        const container = document.getElementById('neuron-graph');
        let width = container.clientWidth;
        let height = container.clientHeight;

        const svg = d3.select("#neuron-graph").append("svg")
            .attr("viewBox", [0, 0, width, height]);

        const colorMap = {{
            "root": "#22d3ee",
            "tool_py": "#a855f7",
            "tool_node": "#10b981",
            "sample": "#f59e0b",
            "data": "#f43f5e",
            "remote_repo": "#3b82f6",
            "directory": "#64748b"
        }};

        const simulation = d3.forceSimulation(graph.nodes)
            .force("link", d3.forceLink(graph.links).id(d => d.id).distance(80))
            .force("charge", d3.forceManyBody().strength(-200))
            .force("center", d3.forceCenter(width / 2, height / 2));

        const link = svg.append("g")
            .selectAll("line")
            .data(graph.links)
            .join("line")
            .attr("class", "neuron-link")
            .style("stroke-opacity", d => (d.source.path === currentPath || d.target.path === currentPath) ? 0.8 : 0.2);

        const node = svg.append("g")
            .selectAll("circle")
            .data(graph.nodes)
            .join("circle")
            .attr("r", d => d.path === currentPath ? 10 : (5 + (d.density * 5)))
            .attr("class", d => "neuron-node" + (d.path === currentPath ? " active" : ""))
            .attr("fill", d => colorMap[d.type] || colorMap["directory"])
            .style("opacity", d => 0.5 + (d.density * 0.5))
            .on("click", (e, d) => window.location.href = (currentPath === "." ? "" : "../".repeat(currentPath.split('/').length)) + d.path + '/readme.html');

        simulation.on("tick", () => {{
            link.attr("x1", d => d.source.x).attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
            node.attr("cx", d => d.x).attr("cy", d => d.y);
        }});

        window.addEventListener("resize", () => {{
            width = container.clientWidth;
            height = container.clientHeight;
            svg.attr("viewBox", [0, 0, width, height]);
            simulation.force("center", d3.forceCenter(width / 2, height / 2)).alpha(0.3).restart();
        }});
    </script>
</body>
</html>
"""

ITEM_ROW = """
<div class="file-row px-6 py-3 flex items-center transition-all {cursor_class}" {onclick_attr}>
    <div class="flex items-center gap-3">
        <span class="{color}">{icon}</span>
        <span class="text-sm font-mono text-slate-200">{name}</span>
    </div>
    <div class="flex-grow"></div>
    <span class="text-[10px] font-mono text-slate-600 uppercase tracking-widest">{type}</span>
</div>
"""

GUIDANCE_MAP = {
    ".ai": "Root configuration and metadata. This node holds the primary architectural blueprints and handoff instructions.",
    ".ai/tools": "System utility hub. Ensure all scripts use ag_core.py for path validation and deterministic time.",
    ".ai/EVIDENCE": "Promotion truth source. Never modify EVID files manually; they are managed by the Promotion Skillset.",
    ".ai/SAMPLES": "Template blueprints for rapid project instantiation and skill discovery.",
    ".ai/STATE": "Procedural memory anchors. Serialized state objects to prevent context amnesia.",
    ".ai/TASKS": "Active mission control for the current loop. Tracks objectives and execution status.",
    ".ai/STREAMS": "Live intent synchronization and return packet flows for multi-agent coordination.",
    ".ai/DECISIONS": "Architectural Decision Record (ADR) locker. Logs the 'why' behind major transitions.",
    ".ai/AGNOSTIC-ORCH": "Protocol definitions for cross-environment orchestration logic.",
    "external_repos": "Federated nodes. Only digest vetted components. Maintain fork isolation to prevent logic leakage.",
    "TEMP": "Turn-localized scratch. Do not store persistent state here; it is subject to automated cleanup protocols."
}

# --- LOGIC ---

def get_token_efficiency(file_path):
    try:
        if file_path.suffix.lower() in ['.html', '.md', '.txt', '.py', '.json', '.js', '.yaml', '.yml', '.css']:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if not content: return 100
            non_white = len(content.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", ""))
            return int((non_white / len(content)) * 100)
    except:
        pass
    return 100

def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"

def get_plans_from_file(dir_path):
    plans = []
    for f in dir_path.glob("*.md"):
        try:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
                matches = re.findall(r'^[*-]\s*(.+)', content, re.M)
                if matches:
                    plans.extend(matches[:3])
                    break
        except: continue
    if not plans:
        plans = ["Maintain architectural integrity within this node.", "Verify token density vs implementation volume.", "Audit node for absolute path leakage."]
    return "".join([f"<li>• {p}</li>" for p in plans[:3]])

def generate_readme(dir_path, root_path, graph_data):
    dir_path = Path(dir_path)
    root_path = Path(root_path)
    rel_path_str = str(dir_path.relative_to(root_path)).replace(os.sep, '/')
    
    items_html = []
    type_stats = {}
    total_size = 0
    efficiencies = []
    
    # Categorize node
    node_type = "directory"
    if rel_path_str.startswith(".ai/tools"): node_type = "tool_py" if any(dir_path.glob("*.py")) else "tool_node"
    elif rel_path_str.startswith(".ai/SAMPLES"): node_type = "sample"
    elif rel_path_str.startswith(".ai/STATE") or rel_path_str.startswith(".ai/EVIDENCE"): node_type = "data"
    elif rel_path_str == ".": node_type = "root"
    elif (dir_path / ".git").exists(): node_type = "remote_repo"

    # Add to graph
    node_id = f"node_{rel_path_str}"
    if not any(n["id"] == node_id for n in graph_data["nodes"]):
        graph_data["nodes"].append({
            "id": node_id,
            "name": Path(rel_path_str).name or "ROOT",
            "path": rel_path_str,
            "type": node_type,
            "size_raw": 0,
            "eff": 100,
            "density": 0.1
        })
    
    current_node = next(n for n in graph_data["nodes"] if n["id"] == node_id)
    try:
        entries = sorted(list(dir_path.iterdir()), key=lambda x: (not x.is_dir(), x.name.lower()))
    except: return 0, 0

    child_folders = len([e for e in entries if e.is_dir()])
    child_files = len(entries) - child_folders
    current_node["density"] = min(1.0, (child_folders * 0.2) + (child_files * 0.05))

    for entry in entries:
        if entry.name in [".git", "__pycache__", "node_modules", ".venv"] or (entry.name.startswith(".") and entry.name != ".ai"):
             continue
        if entry.name == "readme.html": continue

        is_directory = entry.is_dir()
        if is_directory:
            type_label = "folder"
            has_link = True
            link_target = f"{entry.name}/readme.html"
            icon = '<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 16 16"><path d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25V5.25A1.75 1.75 0 0 0 14.25 3.5h-4.5L8.62 1.379A1.75 1.75 0 0 0 7.379 1H1.75Z"></path></svg>'
            color = "text-cyan-400"
            child_rel = str(entry.relative_to(root_path)).replace(os.sep, '/')
            graph_data["links"].append({"source": node_id, "target": f"node_{child_rel}", "type": "nesting"})
        else:
            ext = entry.suffix[1:].lower() if entry.suffix else "file"
            type_label = ext
            try:
                size = entry.stat().st_size
            except (FileNotFoundError, PermissionError):
                size = 0
            total_size += size
            eff = get_token_efficiency(entry)
            efficiencies.append(eff)
            viewable_exts = ['md', 'py', 'json', 'html', 'js', 'txt', 'css', 'yaml', 'yml']
            has_link = ext in viewable_exts
            link_target = entry.name
            icon = '<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 16 16"><path d="M4 0h5.5L14 4.5V14a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h5.5L4 0zm0 1v13a1 1 0 0 0 1 1h7a1 1 0 0 0 1-1V5h-4V1H5a1 1 0 0 0-1 1z"/></svg>'
            color = "text-slate-500" if not has_link else "text-slate-200"
            
        type_stats[type_label] = type_stats.get(type_label, 0) + 1
        cursor_class = "cursor-pointer" if has_link else "cursor-default opacity-60"
        onclick_attr = f'onclick="window.location.href=\'{link_target}\'"' if has_link else ""
        items_html.append(ITEM_ROW.format(cursor_class=cursor_class, onclick_attr=onclick_attr, icon=icon, color=color, name=entry.name, type=type_label))
    
    avg_eff = int(sum(efficiencies)/len(efficiencies)) if efficiencies else 100
    current_node["size_raw"] = total_size
    current_node["eff"] = avg_eff
    
    title = rel_path_str if rel_path_str != "." else "Mission Control"
    guidance = GUIDANCE_MAP.get(rel_path_str, "Standard workspace directory. Maintain clean structure.")
    
    github_link = ""
    if GITHUB_REPO_URL:
        branch = "master"
        gh_path = f"{GITHUB_REPO_URL}/tree/{branch}/{rel_path_str}" if rel_path_str != "." else GITHUB_REPO_URL
        github_link = f'<a href="{gh_path}" target="_blank" class="text-xs font-bold text-cyan-400 hover:text-cyan-300 transition-all uppercase tracking-widest flex items-center gap-2"><svg class="w-3 h-3" fill="currentColor" viewBox="0 0 16 16"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg> View on GitHub</a>'

    html = HTML_TEMPLATE.format(title=title, rel_path=f"ROOT/{rel_path_str}", item_count=len(items_html), items="".join(items_html), parent_link="../readme.html" if rel_path_str != "." else "#", guidance=guidance, total_size=format_size(total_size), efficiency=avg_eff, plans=get_plans_from_file(dir_path), stats_json=json.dumps(type_stats), github_link=github_link, graph_json=json.dumps(graph_data), rel_path_val=rel_path_str)
    with open(dir_path / "readme.html", "w", encoding="utf-8") as f: f.write(html)
    return total_size, avg_eff

def generate_root_dashboard(root_path, global_stats, graph_data):
    root_path = Path(root_path)
    # Correctly replace the placeholders in ROOT_TEMPLATE
    html = ROOT_TEMPLATE.replace("{stats_json}", json.dumps(global_stats))
    html = html.replace("{graph_json}", json.dumps(graph_data))
    html = html.replace("{GITHUB_REPO_URL}", json.dumps(GITHUB_REPO_URL))
    html = html.replace("{rel_path_val}", ".")
    
    with open(root_path / "readme.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Enchanted Root Dashboard Generated.")

def main():
    root = Path.cwd()
    graph_data = {"nodes": [], "links": []}
    targets = [".ai", "external_repos", "TEMP"]
    
    global_stats = {"total_volume_bytes": 0, "avg_efficiency": 0, "directories": 0, "files": 0}
    eff_list = []

    for target in targets:
        target_path = root / target
        if target_path.exists() and target_path.is_dir():
            print(f"Enriching {target_path}...")
            size, eff = generate_readme(target_path, root, graph_data)
            global_stats["total_volume_bytes"] += size
            global_stats["directories"] += 1
            eff_list.append(eff)
            for dirpath, dirnames, filenames in os.walk(target_path):
                dirnames[:] = [d for d in dirnames if not d.startswith(".") or d == ".ai"]
                for d in dirnames:
                    full_p = Path(dirpath) / d
                    size, eff = generate_readme(full_p, root, graph_data)
                    global_stats["total_volume_bytes"] += size
                    global_stats["directories"] += 1
                    global_stats["files"] += len(list(full_p.glob("*")))
                    eff_list.append(eff)

    global_stats["avg_efficiency"] = int(sum(eff_list)/len(eff_list)) if eff_list else 100
    with open(root / ".ai" / "workspace_graph.json", "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2)
    
    git_path = root / ".ai" / "git_status.json"
    if git_path.exists(): global_stats["git_pulse"] = json.loads(git_path.read_text())
    hoist_path = root / ".ai" / "dep_hoist_audit.json"
    if hoist_path.exists(): global_stats["dep_hoist"] = json.loads(hoist_path.read_text())

    generate_root_dashboard(root, global_stats, graph_data)
    print("Architectural Neural Export Complete.")

if __name__ == "__main__":
    main()
