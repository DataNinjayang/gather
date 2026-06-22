"""
GitHub Pages 部署脚本 - 企业数据智能分析平台链接导航主页
========================================================
使用方法:
  1. 确保已安装 git 和 gh (GitHub CLI)
  2. 运行: python deploy_to_github.py
  3. 按照提示完成操作

依赖安装:
  pip install PyGithub --break-system-packages
"""

import os
import subprocess
import sys

# ============================================================
# 配置区域 - 根据你的实际情况修改以下参数
# ============================================================

# GitHub 仓库信息
GITHUB_USERNAME = "DataNinjayang"  # 你的 GitHub 用户名
REPO_NAME = "link-hub"            # 仓库名称（建议保持 link-hub）
REPO_DESCRIPTION = "企业数据智能分析平台 - 链接导航主页"
IS_PUBLIC = True                  # True=公开仓库, False=私有仓库

# 本地项目路径（存放 HTML 和 assets 的目录）
# 如果脚本放在 link-hub 目录内，使用当前目录即可
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# GitHub Pages 分支
PAGES_BRANCH = "gh-pages"

# ============================================================
# 以下为自动执行逻辑，一般不需要修改
# ============================================================


def run_cmd(cmd, cwd=None, check=True):
    """执行 shell 命令并返回输出"""
    print(f"  > {cmd}")
    result = subprocess.run(
        cmd, shell=True, cwd=cwd or PROJECT_DIR,
        capture_output=True, text=True
    )
    if result.stdout:
        print(f"    {result.stdout.strip()}")
    if result.stderr:
        print(f"    [stderr] {result.stderr.strip()}")
    if check and result.returncode != 0:
        print(f"    [错误] 命令执行失败，返回码: {result.returncode}")
        sys.exit(1)
    return result


def step1_check_prerequisites():
    """步骤1: 检查前置条件"""
    print("\n" + "=" * 60)
    print("步骤 1/5: 检查前置条件")
    print("=" * 60)

    # 检查 git
    result = run_cmd("git --version", check=False)
    if result.returncode != 0:
        print("  [错误] 未安装 git，请先安装: https://git-scm.com/")
        sys.exit(1)

    # 检查 gh
    result = run_cmd("gh --version", check=False)
    if result.returncode != 0:
        print("  [错误] 未安装 GitHub CLI (gh)，请先安装:")
        print("         https://cli.github.com/")
        sys.exit(1)

    # 检查 gh 登录状态
    result = run_cmd("gh auth status", check=False)
    if result.returncode != 0:
        print("  [提示] GitHub CLI 未登录，正在尝试登录...")
        print("         请按照浏览器提示完成授权")
        run_cmd("gh auth login --web")
    else:
        print("  [OK] Git 已安装")
        print("  [OK] GitHub CLI 已安装且已登录")

    # 检查项目文件
    html_file = os.path.join(PROJECT_DIR, "link-hub.html")
    assets_dir = os.path.join(PROJECT_DIR, "assets")
    if not os.path.exists(html_file):
        print(f"  [错误] 未找到 HTML 文件: {html_file}")
        print(f"         请确保脚本放在 link-hub 项目根目录下")
        sys.exit(1)
    if not os.path.exists(assets_dir):
        print(f"  [错误] 未找到 assets 目录: {assets_dir}")
        sys.exit(1)

    print("  [OK] 项目文件检查通过")


def step2_init_git():
    """步骤2: 初始化 Git 仓库"""
    print("\n" + "=" * 60)
    print("步骤 2/5: 初始化 Git 仓库")
    print("=" * 60)

    git_dir = os.path.join(PROJECT_DIR, ".git")
    if os.path.exists(git_dir):
        print("  [OK] Git 仓库已存在，跳过初始化")
    else:
        run_cmd("git init")
        print("  [OK] Git 仓库初始化完成")

    # 创建 .gitignore
    gitignore_path = os.path.join(PROJECT_DIR, ".gitignore")
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.write("# Python\n__pycache__/\n*.pyc\n*.pyo\n*.egg-info/\n")
            f.write("\n# IDE\n.vscode/\n.idea/\n")
            f.write("\n# OS\n.DS_Store\nThumbs.db\n")
            f.write("\n# Temp\n*.tmp\n*.log\n")
        print("  [OK] 已创建 .gitignore")


def step3_create_github_repo():
    """步骤3: 创建 GitHub 远程仓库"""
    print("\n" + "=" * 60)
    print("步骤 3/5: 创建 GitHub 远程仓库")
    print("=" * 60)

    full_repo = f"{GITHUB_USERNAME}/{REPO_NAME}"

    # 检查远程仓库是否已存在
    result = run_cmd(f"gh repo view {full_repo}", check=False)
    if result.returncode == 0:
        print(f"  [OK] 仓库已存在: https://github.com/{full_repo}")
    else:
        visibility = "--public" if IS_PUBLIC else "--private"
        run_cmd(
            f'gh repo create {full_repo} '
            f'--description "{REPO_DESCRIPTION}" '
            f'{visibility} '
            f'--source="{PROJECT_DIR}" '
            f'--push=false'
        )
        print(f"  [OK] 仓库创建成功: https://github.com/{full_repo}")

    # 设置远程仓库地址
    run_cmd(f"git remote remove origin", check=False)
    run_cmd(f"git remote add origin https://github.com/{full_repo}.git")
    print(f"  [OK] 远程仓库地址已设置")


def step4_commit_and_push():
    """步骤4: 提交代码并推送到 GitHub"""
    print("\n" + "=" * 60)
    print("步骤 4/5: 提交代码并推送")
    print("=" * 60)

    # 添加所有文件
    run_cmd("git add -A")

    # 检查是否有变更
    result = run_cmd("git status --porcelain", check=False)
    if not result.stdout.strip():
        print("  [OK] 没有新的变更需要提交")
    else:
        run_cmd('git commit -m "feat: 初始化企业数据智能分析平台链接导航主页"')
        print("  [OK] 代码已提交")

    # 推送到 main 分支
    run_cmd("git branch -M main", check=False)
    run_cmd("git push -u origin main", check=False)
    # 如果 push 失败，尝试强制推送
    if result.returncode != 0:
        run_cmd("git push -u origin main --force", check=False)
    print("  [OK] 代码已推送到 main 分支")


def step5_enable_github_pages():
    """步骤5: 启用 GitHub Pages"""
    print("\n" + "=" * 60)
    print("步骤 5/5: 配置 GitHub Pages")
    print("=" * 60)

    full_repo = f"{GITHUB_USERNAME}/{REPO_NAME}"

    # 使用 gh api 启用 GitHub Pages（从 main 分支根目录部署）
    run_cmd(
        f'gh api -X PUT repos/{full_repo}/pages '
        f'-f source.branch=main '
        f'-f source.path=/ '
        f'-f build_type=legacy '
        f'--input - <<< \'{{"source":{"branch":"main","path":"/"},"build_type":"legacy"}}\'',
        check=False
    )

    # 备用方案：使用 gh api 的 JSON 方式
    result = subprocess.run(
        f'gh api -X POST repos/{full_repo}/pages '
        f'-f source[branch]=main '
        f'-f source[path]=/',
        shell=True, capture_output=True, text=True, cwd=PROJECT_DIR
    )

    if result.returncode == 0:
        print("  [OK] GitHub Pages 已启用")
    else:
        # 尝试 PUT 方式
        result2 = subprocess.run(
            f'gh api -X PUT repos/{full_repo}/pages '
            f'-F source=main',
            shell=True, capture_output=True, text=True, cwd=PROJECT_DIR
        )
        if result2.returncode == 0:
            print("  [OK] GitHub Pages 已启用")
        else:
            print("  [提示] GitHub Pages 自动配置可能未成功")
            print("         请手动前往以下地址启用:")
            print(f"         https://github.com/{full_repo}/settings/pages")
            print("         选择 Source: Deploy from a branch")
            print("         Branch: main / (root)")
            print("         然后点击 Save")

    print(f"\n  访问地址: https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/")
    print(f"  仓库地址: https://github.com/{full_repo}")


def main():
    print("=" * 60)
    print("  企业数据智能分析平台 - GitHub Pages 部署工具")
    print("=" * 60)
    print(f"  项目目录: {PROJECT_DIR}")
    print(f"  目标仓库: {GITHUB_USERNAME}/{REPO_NAME}")
    print(f"  仓库描述: {REPO_DESCRIPTION}")
    print(f"  公开仓库: {'是' if IS_PUBLIC else '否'}")

    try:
        step1_check_prerequisites()
        step2_init_git()
        step3_create_github_repo()
        step4_commit_and_push()
        step5_enable_github_pages()

        print("\n" + "=" * 60)
        print("  部署完成!")
        print("=" * 60)
        print(f"\n  网站地址: https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/")
        print(f"  仓库地址: https://github.com/{GITHUB_USERNAME}/{REPO_NAME}")
        print("\n  注意: GitHub Pages 部署可能需要 1-3 分钟生效")
        print("  如果页面未更新，请稍等片刻后刷新\n")

    except KeyboardInterrupt:
        print("\n\n  [已取消] 用户中断了部署流程")
        sys.exit(0)
    except Exception as e:
        print(f"\n  [错误] 部署过程中出现异常: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
