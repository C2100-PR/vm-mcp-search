from typing import List, Dict
import os
import json
from google.cloud import storage
from google.cloud import automl

class MCPSearchEngine:
    """Core search engine for MCP capabilities"""
    
    def __init__(self):
        self.index = {}
        self.capabilities = {
            'professional': self._init_professional_services(),
            'security': self._init_security_services(),
            'development': self._init_development_services(),
            'ml': self._init_ml_services(),
            'scanning': self._init_scanning_services()
        }

    def _init_professional_services(self):
        return {
            'terraform': {'path': '/opt/mcp/professional-services/terraform'},
            'architecture': {'path': '/opt/mcp/professional-services/architecture'},
            'migration': {'path': '/opt/mcp/professional-services/migration'}
        }

    def _init_security_services(self):
        return {
            'policy': {'path': '/opt/mcp/forseti-security/policy'},
            'compliance': {'path': '/opt/mcp/forseti-security/compliance'},
            'monitoring': {'path': '/opt/mcp/forseti-security/monitoring'}
        }

    def _init_development_services(self):
        return {
            'python': {'path': '/opt/mcp/getting-started-python/python'},
            'containers': {'path': '/opt/mcp/getting-started-python/containers'},
            'apis': {'path': '/opt/mcp/getting-started-python/apis'}
        }

    def _init_ml_services(self):
        return {
            'pipelines': {'path': '/opt/mcp/ml-on-gcp/pipelines'},
            'models': {'path': '/opt/mcp/ml-on-gcp/models'},
            'training': {'path': '/opt/mcp/ml-on-gcp/training'}
        }

    def _init_scanning_services(self):
        return {
            'resources': {'path': '/opt/mcp/gcp_scanner/resources'},
            'network': {'path': '/opt/mcp/gcp_scanner/network'},
            'iam': {'path': '/opt/mcp/gcp_scanner/iam'}
        }

    def search(self, query: str, category: str = None) -> List[Dict]:
        """
        Search through MCP capabilities
        
        Args:
            query: Search query string
            category: Optional category to limit search
            
        Returns:
            List of matching capabilities
        """
        results = []
        search_space = self.capabilities.get(category, self.capabilities) if category else self.capabilities
        
        for cat, services in search_space.items():
            for service, details in services.items():
                if query.lower() in service.lower():
                    results.append({
                        'category': cat,
                        'service': service,
                        'details': details
                    })
                    
        return results

    def get_capability_details(self, category: str, service: str) -> Dict:
        """Get detailed information about a specific capability"""
        if category in self.capabilities and service in self.capabilities[category]:
            return self.capabilities[category][service]
        return None

    def update_index(self):
        """Update search index with latest capability information"""
        for category, services in self.capabilities.items():
            for service, details in services.items():
                path = details['path']
                if os.path.exists(path):
                    # Index content for searching
                    with open(path, 'r') as f:
                        content = f.read()
                        self.index[f"{category}/{service}"] = content