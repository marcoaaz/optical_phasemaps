import re
import os
import subprocess
import shutil  # Required for copying your images

def setup_sphinx(docs_root):
    """Restores Sphinx documentation to the default look."""
    source_dir = os.path.join(docs_root, 'source')
    static_css_dir = os.path.join(source_dir, '_static', 'css')
    
    os.makedirs(static_css_dir, exist_ok=True)
    with open(os.path.join(static_css_dir, 'custom.css'), 'w', encoding='utf-8') as f:
        f.write("/* Default styles restored */")

    conf_content = """
project = 'Optical Phase Maps: Documentation'
copyright = '2026, Marco Acevedo'
author = 'Marco A. Acevedo Z.'

extensions = [
    'sphinx_design',
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages'
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}
"""
    with open(os.path.join(source_dir, 'conf.py'), 'w', encoding='utf-8') as f:
        f.write(conf_content)

    index_content = """
Documentation Hub
=================

Welcome to the mineralogy analysis documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   image_analysis_pipeline 
   cube_converter
   chemistry_simplifier
   phase_interpreter
   pipeline_workshop
"""
    with open(os.path.join(source_dir, 'index.rst'), 'w', encoding='utf-8') as f:
        f.write(index_content)

def sanitize_rst(rst_path):
    """Aggressively removes all container directives to prevent Sphinx errors."""
    with open(rst_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = [line for line in lines if ".. container::" not in line]
    with open(rst_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

def convert_to_rst(tex_filepath):
    """Calls Pandoc to convert Tex to RST and then sanitizes the output."""
    rst_filepath = tex_filepath.replace('.tex', '.rst')
    subprocess.run(['pandoc', tex_filepath, '-o', rst_filepath], check=True)
    sanitize_rst(rst_filepath)

def split_tex_by_chapter(input_file, source_folder):
    """Splits LaTeX, migrates images, and triggers Pandoc."""
    # --- NEW: Image Migration Logic ---
    tex_dir = os.path.dirname(input_file)
    media_src = os.path.join(tex_dir, 'media')
    media_dest = os.path.join(source_folder, 'media')

    if os.path.exists(media_src):
        if os.path.exists(media_dest):
            shutil.rmtree(media_dest)
        shutil.copytree(media_src, media_dest)
        print(f"Successfully migrated images to: {media_dest}")
    # ----------------------------------

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().replace(r'\end{document}', '')

    chapters = re.split(r'\\chapter\{([^}]+)\}', content)
    for i in range(1, len(chapters), 2):
        title = chapters[i].strip()
        body = chapters[i+1].strip()
        file_name = f"{title.lower().replace(' ', '_')}.tex"
        file_path = os.path.join(source_folder, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"\\section{{{title}}}\n{body}")
        
        convert_to_rst(file_path)

def build_html(docs_root):
    """Builds to /docs folder and creates .nojekyll for GitHub Pages."""
    source_dir = os.path.join(docs_root, 'source')
    build_dir = os.path.join(docs_root, 'docs') 
    
    # Ensure build directory exists
    os.makedirs(build_dir, exist_ok=True)
    
    subprocess.run(['sphinx-build', '-E', '-a', '-b', 'html', source_dir, build_dir], check=True)
    
    # Bypass Jekyll for GitHub Pages
    open(os.path.join(build_dir, '.nojekyll'), 'a').close()
    print(f"\n--- SUCCESS ---\nWebsite built at: {build_dir}/index.html")

if __name__ == "__main__":
    
    # docs_root = r"E:\Alienware_March 22\current work\00-new code May_22\generate_documentation"

    input_tex = r"C:\Users\acevedoz\OneDrive - Queensland University of Technology\Desktop\software_docs\document_v3.tex"    
    docs_root = r"C:\Users\acevedoz\OneDrive - Queensland University of Technology\Desktop\software_docs\github_data"
    source_dir = os.path.join(docs_root, 'source')

    setup_sphinx(docs_root)
    split_tex_by_chapter(input_tex, source_dir)
    build_html(docs_root)