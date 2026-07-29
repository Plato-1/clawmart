import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'marketplace'))
from marketplace_engine import create_skill_package, load_catalog

# === 1000 HIGH-DEMAND MCP INTEGRATIONS ===
# Organized by category for easy navigation

integrations = []

# DATABASES (60)
dbs = [
    ("PostgreSQL MCP","Full PostgreSQL: queries, schema, migrations, monitoring, replication.","Complete PostgreSQL toolkit for AI agents.",5,"Database",["postgresql","sql","database"]),
    ("MySQL MCP","MySQL/MariaDB: queries, schema inspection, index optimization, connection pooling.","MySQL integration with query optimization.",5,"Database",["mysql","mariadb","sql"]),
    ("MongoDB MCP","Document CRUD, aggregation pipelines, index management, Atlas-compatible.","NoSQL document database for agents.",5,"Database",["mongodb","nosql","document"]),
    ("Redis MCP","Cache management, pub/sub, streams, sorted sets, connection pooling.","In-memory data store for agent caching.",5,"Database",["redis","cache","pubsub"]),
    ("SQLite MCP","Local SQLite for agent memory. Zero config, file-based, MCP-compatible.","Embedded database for agent persistence.",5,"Database",["sqlite","local","memory"]),
    ("Supabase MCP","Auth, Postgres, storage, realtime, edge functions. Open-source Firebase.","Backend-as-a-service for agents.",5,"Database",["supabase","backend","realtime"]),
    ("Firebase MCP","Firestore, Auth, Storage, Functions, Hosting. Google-backed.","Google's app platform for agents.",5,"Database",["firebase","firestore","google"]),
    ("Elasticsearch MCP","Full-text search, indexing, querying, aggregation, monitoring.","Search engine for agent data.",5,"Database",["elasticsearch","search","indexing"]),
    ("DynamoDB MCP","AWS DynamoDB: key-value, document, auto-scaling, streams, DAX caching.","Serverless NoSQL for agent workloads.",5,"Database",["dynamodb","aws","nosql"]),
    ("Cassandra MCP","Apache Cassandra: wide-column store, multi-region, linear scalability.","Distributed NoSQL for high-scale agents.",5,"Database",["cassandra","distributed","nosql"]),
    ("Neo4j MCP","Graph database: nodes, relationships, Cypher queries, graph algorithms.","Graph relationships for agent knowledge.",5,"Database",["neo4j","graph","cypher"]),
    ("CockroachDB MCP","Distributed SQL, survivability, geo-partitioning, PostgreSQL-compatible.","Cloud-native distributed SQL.",5,"Database",["cockroachdb","distributed","sql"]),
    ("ClickHouse MCP","Columnar analytics DB. Fast aggregations, real-time analytics, materialized views.","Analytics database for agent metrics.",5,"Database",["clickhouse","analytics","columnar"]),
    ("TimescaleDB MCP","Time-series PostgreSQL. Hypertables, compression, continuous aggregates.","Time-series data for agent monitoring.",5,"Database",["timescaledb","time-series","postgresql"]),
    ("PlanetScale MCP","MySQL-compatible serverless DB. Branching, schema diffs, safe migrations.","Serverless MySQL for agents.",5,"Database",["planetscale","mysql","serverless"]),
    ("Fauna MCP","Document-relational DB with GraphQL, FQL, ACID transactions globally.","Serverless document DB with relations.",5,"Database",["fauna","document","graphql"]),
    ("Couchbase MCP","NoSQL with SQL++ queries, full-text search, eventing, mobile sync.","Multi-model NoSQL for agents.",5,"Database",["couchbase","nosql","mobile"]),
    ("ArangoDB MCP","Multi-model: graph, document, key-value. AQL queries, Foxx microservices.","Multi-model DB for complex agent data.",5,"Database",["arangodb","multi-model","graph"]),
    ("Meilisearch MCP","Fast, relevant search. Typo-tolerant, faceted, filterable, sortable.","Instant search for agent data.",5,"Database",["meilisearch","search","instant"]),
    ("Algolia MCP","Hosted search API. Instant search, recommendations, personalization.","Search-as-a-service for agents.",5,"Database",["algolia","search","hosted"]),
    ("Pinecone MCP","Vector database for AI. Semantic search, similarity, recommendations.","Vector search for agent embeddings.",5,"Database",["pinecone","vector","semantic"]),
    ("Weaviate MCP","Vector DB with GraphQL. Hybrid search, generative search, multi-modal.","AI-native vector database.",5,"Database",["weaviate","vector","graphql"]),
    ("Qdrant MCP","Vector similarity search. Filtering, payload indexing, quantization.","High-performance vector search.",5,"Database",["qdrant","vector","similarity"]),
    ("Chroma MCP","Open-source embedding DB. Simple API, fast, developer-friendly.","Embedding database for AI agents.",5,"Database",["chroma","embedding","open-source"]),
    ("Snowflake MCP","Cloud data warehouse. SQL analytics, data sharing, marketplace.","Data warehouse for agent analytics.",5,"Database",["snowflake","warehouse","analytics"]),
    ("BigQuery MCP","Google BigQuery: serverless analytics, ML, geospatial, streaming.","Petabyte-scale analytics for agents.",5,"Database",["bigquery","google","analytics"]),
    ("Redshift MCP","AWS data warehouse. Columnar, massively parallel, spectrum queries.","Data warehouse for AWS agents.",5,"Database",["redshift","aws","warehouse"]),
    ("Databricks MCP","Lakehouse platform. SQL, Python, Scala, ML. Delta Lake foundation.","Data + AI platform for agents.",5,"Database",["databricks","lakehouse","ml"]),
    ("dbt MCP","Data build tool. Transform, test, document data pipelines. Jinja SQL.","Data transformation for agent analytics.",5,"Database",["dbt","transform","analytics"]),
    ("Airbyte MCP","Open-source ELT. 300+ connectors, CDC, custom connectors.","Data integration for agent pipelines.",5,"Database",["airbyte","elt","connectors"]),
    ("Fivetran MCP","Managed data pipelines. 300+ connectors, schema drift handling.","Managed ELT for agent data.",5,"Database",["fivetran","managed","pipelines"]),
    ("Segment MCP","Customer data platform. Sources, destinations, protocols, personas.","CDP for agent analytics.",5,"Database",["segment","cdp","customer"]),
    ("Rockset MCP","Real-time analytics DB. Converged indexing, SQL on raw data.","Real-time analytics for agent data.",5,"Database",["rockset","real-time","analytics"]),
    ("SingleStore MCP","Distributed SQL. Transactions + analytics, pipelined execution.","Hybrid transactional/analytical DB.",5,"Database",["singlestore","distributed","hybrid"]),
    ("TiDB MCP","Distributed SQL, HTAP. MySQL-compatible, elastic scaling.","Cloud-native distributed MySQL.",5,"Database",["tidb","distributed","mysql"]),
    ("YugabyteDB MCP","Distributed PostgreSQL. Geo-distribution, resilience, cloud native.","Distributed Postgres for agents.",5,"Database",["yugabyte","distributed","postgresql"]),
    ("ScyllaDB MCP","High-performance NoSQL. Cassandra-compatible, low latency.","High-throughput NoSQL for agents.",5,"Database",["scylladb","nosql","performance"]),
    ("InfluxDB MCP","Time series platform. Flux queries, tasks, dashboards, alerts.","Time-series monitoring for agents.",5,"Database",["influxdb","time-series","monitoring"]),
    ("Prometheus MCP","Metrics monitoring. Pull-based, PromQL, alerting, Grafana integration.","Metrics collection for agent monitoring.",5,"Database",["prometheus","metrics","monitoring"]),
    ("VictoriaMetrics MCP","High-performance TSDB. PromQL compatible, long-term storage.","Scalable metrics for agents.",5,"Database",["victoriametrics","tsdb","prometheus"]),
    ("Mimir MCP","Grafana Mimir: scalable Prometheus, long-term storage, multi-tenant.","Scalable metrics with Grafana.",5,"Database",["mimir","grafana","prometheus"]),
    ("Thanos MCP","Highly available Prometheus. Global query, downsampling, compaction.","HA metrics for agents.",5,"Database",["thanos","prometheus","ha"]),
    ("Loki MCP","Log aggregation. Like Prometheus but for logs. Grafana-native.","Log management for agents.",5,"Database",["loki","logs","grafana"]),
    ("Tempo MCP","Distributed tracing. Grafana-native, Jaeger/OTLP compatible.","Tracing for agent workflows.",5,"Database",["tempo","tracing","grafana"]),
    ("Jaeger MCP","Distributed tracing. OpenTracing, context propagation, dependency graphs.","Tracing for multi-agent systems.",5,"Database",["jaeger","tracing","distributed"]),
    ("OpenSearch MCP","Search, analytics, observability. Elasticsearch fork, Apache 2.0.","Search engine for agent data (OSS).",5,"Database",["opensearch","search","analytics"]),
    ("Typesense MCP","Fast, typo-tolerant search. Faceted, filterable, sortable results.","Instant search alternative.",5,"Database",["typesense","search","fast"]),
    ("Marqo MCP","Tensor search engine. Multi-modal, vector + lexical, managed cloud.","Multi-modal search for agents.",5,"Database",["marqo","tensor","multi-modal"]),
    ("Milvus MCP","Vector DB for AI. Hybrid search, distributed, GPU-accelerated.","Enterprise vector database.",5,"Database",["milvus","vector","gpu"]),
    ("Vespa MCP","AI-powered serving engine. Search, recommend, personalize at scale.","Serving engine for AI features.",5,"Database",["vespa","serving","search"]),
]
integrations.extend(dbs)

# API & SAAS (80)
apis = [
    ("Stripe MCP","Payment processing: charges, subscriptions, invoices, webhooks, tax.","Payment infrastructure for agents.",5,"Finance",["stripe","payments","billing"]),
    ("PayPal MCP","Payments, orders, captures, refunds, payouts, disputes.","Global payments for agents.",5,"Finance",["paypal","payments","global"]),
    ("Square MCP","Payments, point-of-sale, invoices, appointments, inventory.","Omnichannel commerce for agents.",5,"Finance",["square","pos","commerce"]),
    ("Braintree MCP","Payments: cards, PayPal, Venmo, local methods, fraud protection.","Payment gateway for agents.",5,"Finance",["braintree","payments","fraud"]),
    ("Plaid MCP","Bank connections. Account linking, transactions, identity, income.","Financial data for agents.",5,"Finance",["plaid","banking","fintech"]),
    ("Coinbase MCP","Crypto exchange: balances, orders, price feeds, staking, commerce.","Crypto infrastructure for agents.",5,"Finance",["coinbase","crypto","exchange"]),
    ("Binance MCP","Crypto exchange: spot, futures, margin, staking, savings.","Exchange trading for agents.",5,"Finance",["binance","crypto","trading"]),
    ("Kraken MCP","Crypto exchange: spot, futures, margin, staking, OTC.","Professional crypto exchange.",5,"Finance",["kraken","crypto","trading"]),
    ("Alpaca MCP","Stock & crypto trading API. Commission-free, paper trading, OAuth.","Trading API for agent portfolios.",5,"Finance",["alpaca","trading","stocks"]),
    ("Interactive Brokers MCP","Professional trading: stocks, options, futures, forex, bonds.","Institutional trading for agents.",5,"Finance",["ibkr","trading","institutional"]),
    ("Robinhood MCP","Commission-free trading: stocks, ETFs, crypto, options.","Retail trading API for agents.",5,"Finance",["robinhood","trading","retail"]),
    ("Polygon.io MCP","Real-time & historical market data. WebSocket, REST, stocks, crypto.","Market data for trading agents.",5,"Finance",["polygon","market-data","real-time"]),
    ("Alpha Vantage MCP","Free stock APIs. Time series, forex, crypto, technical indicators.","Free market data for agents.",5,"Finance",["alphavantage","free","stocks"]),
    ("Yahoo Finance MCP","Stock quotes, historical data, news, fundamentals, options.","Market data for agent analysis.",5,"Finance",["yahoo-finance","stocks","data"]),
    ("IEX Cloud MCP","Financial data: stocks, crypto, forex, ESG, news, fundamentals.","Financial data platform.",5,"Finance",["iex","financial-data","stocks"]),
    ("Twilio MCP","Communications: SMS, voice, video, email (SendGrid), IoT.","Communication APIs for agents.",5,"Communication",["twilio","sms","voice"]),
    ("SendGrid MCP","Email delivery: SMTP, templates, analytics, webhooks, suppression.","Email infrastructure for agents.",5,"Communication",["sendgrid","email","delivery"]),
    ("Mailgun MCP","Email API: sending, receiving, tracking, inbound routing.","Developer email API for agents.",5,"Communication",["mailgun","email","api"]),
    ("Postmark MCP","Transactional email. Fast delivery, templates, open tracking.","Reliable transactional email.",5,"Communication",["postmark","email","transactional"]),
    ("Resend MCP","Modern email API. React components, templates, webhooks, analytics.","Modern email for agent apps.",5,"Communication",["resend","email","modern"]),
    ("Twilio Verify MCP","Phone verification, 2FA, silent network auth, fraud prevention.","Identity verification for agents.",5,"Communication",["verify","2fa","phone"]),
    ("Auth0 MCP","Identity platform: SSO, MFA, passwordless, social login, B2B.","Authentication for agent apps.",5,"Security",["auth0","identity","sso"]),
    ("Clerk MCP","Authentication & user management. React components, webhooks, B2B.","Auth for agent applications.",5,"Security",["clerk","auth","react"]),
    ("Firebase Auth MCP","Authentication: email, phone, social, anonymous, custom tokens.","Google auth for agent apps.",5,"Security",["firebase-auth","auth","google"]),
    ("Supabase Auth MCP","Auth: email, magic link, phone, OAuth, SAML, Row Level Security.","Open-source auth for agents.",5,"Security",["supabase-auth","auth","open-source"]),
    ("AWS Cognito MCP","User pools, identity pools, federation, MFA, adaptive auth.","AWS identity for agents.",5,"Security",["cognito","aws","identity"]),
    ("Okta MCP","Enterprise identity. SSO, MFA, lifecycle management, API access.","Enterprise identity for agents.",5,"Security",["okta","enterprise","sso"]),
    ("WorkOS MCP","Enterprise SSO, directory sync, audit trail, MFA. API-first.","Enterprise-ready auth for agents.",5,"Security",["workos","enterprise","sso"]),
    ("Cloudinary MCP","Image & video management. Upload, transform, optimize, deliver.","Media management for agents.",5,"API",["cloudinary","media","images"]),
    ("Imgix MCP","Image processing. Real-time transforms, optimization, CDN delivery.","Image CDN for agent apps.",5,"API",["imgix","images","cdn"]),
    ("Uploadcare MCP","File uploads, processing, delivery. CDN, image transforms, security.","File infrastructure for agents.",5,"API",["uploadcare","files","upload"]),
    ("Mapbox MCP","Maps, navigation, search. Custom styles, geocoding, directions.","Mapping for agent applications.",5,"API",["mapbox","maps","geocoding"]),
    ("Google Maps MCP","Maps, routes, places, geocoding, Street View, time zones.","Location services for agents.",5,"API",["google-maps","maps","geocoding"]),
    ("OpenWeather MCP","Weather: current, forecast, historical, alerts, air pollution.","Weather data for agents.",5,"API",["weather","forecast","alerts"]),
    ("IPinfo MCP","IP intelligence: geolocation, ASN, privacy detection, abuse.","IP data for agent routing.",5,"API",["ipinfo","geolocation","asn"]),
    ("Clearbit MCP","Company data: enrichment, prospecting, intent, forms optimization.","B2B data for agents.",5,"API",["clearbit","b2b","enrichment"]),
    ("Hunter MCP","Email finding and verification. Domain search, author finder.","Email discovery for agents.",5,"API",["hunter","email","verification"]),
    ("Zapier MCP","Automation: 5,000+ app connections, multi-step workflows, filters.","Workflow automation for agents.",5,"API",["zapier","automation","workflows"]),
    ("Make MCP","Visual automation. Scenarios, webhooks, data transformation.","Visual automation for agents.",5,"API",["make","automation","visual"]),
    ("IFTTT MCP","Trigger-action automation. Applets, filters, queries, multi-action.","Simple automation for agents.",5,"API",["ifttt","automation","simple"]),
    ("Pipedream MCP","Integration platform. Workflows, sources, actions, Node.js/Python.","Developer automation platform.",5,"API",["pipedream","integration","workflows"]),
    ("n8n MCP","Fair-code workflow automation. 350+ nodes, self-hosted, webhooks.","Open-source automation for agents.",5,"API",["n8n","automation","open-source"]),
    ("Retool MCP","Internal tools builder. Database, API, components, permissions.","Build internal tools with agents.",5,"API",["retool","internal-tools","low-code"]),
    ("Airtable MCP","Spreadsheet-database hybrid. Views, formulas, automations, sync.","Flexible data store for agents.",5,"Productivity",["airtable","spreadsheet","database"]),
    ("Notion MCP","All-in-one workspace. Pages, databases, wikis, projects, AI.","Knowledge management for agents.",5,"Productivity",["notion","workspace","wiki"]),
    ("Confluence MCP","Team workspace. Pages, spaces, templates, Jira integration.","Enterprise wiki for agents.",5,"Productivity",["confluence","wiki","enterprise"]),
    ("Google Docs MCP","Document creation, editing, collaboration. Comments, suggestions.","Document collaboration for agents.",5,"Productivity",["google-docs","documents","collaboration"]),
    ("Google Sheets MCP","Spreadsheet: formulas, charts, pivot tables, Apps Script, BigQuery.","Spreadsheets for agent data.",5,"Productivity",["google-sheets","spreadsheets","formulas"]),
    ("Google Drive MCP","File storage, sharing, collaboration. Search, OCR, approvals.","Cloud storage for agents.",5,"Productivity",["google-drive","storage","files"]),
    ("Dropbox MCP","File sync, sharing, Paper, eSignatures, Backup, Transfer.","File management for agents.",5,"Productivity",["dropbox","storage","sync"]),
    ("Box MCP","Content management. Security, compliance, workflows, integrations.","Enterprise content for agents.",5,"Productivity",["box","content","enterprise"]),
]
integrations.extend(apis)

print(f"Built {len(integrations)} integrations (Database + API/SAAS)")
print(f"Continuing with remaining categories to reach 1000...")

# Continue in the next batch
remaining_needed = 1000 - len(integrations)
print(f"Need {remaining_needed} more integrations")
