<div align="center">

![Image](https://github.com/user-attachments/assets/84e342ee-e85b-4e52-8a9a-337181f65091)

# 🔍 Research Bot

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

マルチエージェントによる高度な研究支援ボット  
Web検索と情報統合を自動化し、包括的なレポートを生成

</div>

## 📚 目次
- [機能概要](#機能概要)
- [必要要件](#必要要件)
- [インストール](#インストール)
- [使用方法](#使用方法)
- [アーキテクチャ](#アーキテクチャ)
- [改善提案](#改善提案)

## 🌟 機能概要

Research Botは、研究プロセスを自動化し、効率化するためのツールです。複数のAIエージェントが協調して動作し、包括的な研究レポートを生成します。

### 主な機能：
- 🔎 インテリジェントなWeb検索計画の立案
- 📊 並列処理による効率的な情報収集
- 📝 構造化されたレポートの自動生成
- 💡 関連する追加研究トピックの提案

## 💻 必要要件

- Python 3.9以上
- OpenAI APIキー
- インターネット接続

## 🚀 インストール

```bash
# リポジトリのクローン
git clone https://github.com/username/research-bot.git
cd research-bot

# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt

# 環境変数の設定
cp .env.example .env
# .envファイルを編集してAPIキーを設定
```

## 🎯 使用方法

1. 環境設定が完了したら、以下のコマンドで実行：
```bash
python -m examples.research_bot.main
```

2. プロンプトが表示されたら、研究したいトピックを入力します。

3. ボットが以下のステップを実行します：
   - 検索計画の立案
   - 情報収集と要約
   - 最終レポートの生成

## 🏗 アーキテクチャ

システムは3つの主要なエージェントで構成されています：

1. **Planner Agent** (`planner_agent`)
   - 研究トピックの分析
   - 効果的な検索クエリの生成
   - 検索戦略の最適化

2. **Search Agent** (`search_agent`)
   - Web検索の実行
   - 結果の要約と重要点の抽出
   - 並列処理による効率的な情報収集

3. **Writer Agent** (`writer_agent`)
   - 収集情報の統合
   - 構造化されたレポートの生成
   - フォローアップ質問の提案

