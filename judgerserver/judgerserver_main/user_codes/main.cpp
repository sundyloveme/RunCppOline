#include<bits/stdc++.h>
using namespace std;
int n,ans=-1,an=0,yc[30][30],vis[30];
char ch;
string tr[30];
int mt(int x,int y)
{
	bool pp=true;
	int ky=0;
	for(int k=tr[x].size()-1;k>=0;k--)
	{
		for(int kx=k;kx<tr[x].size();kx++)
			if(tr[x][kx]!=tr[y][ky++])
			{
				pp=false;
				break;
			}
		if(pp==true)
			return tr[x].size()-k;
		ky=0;
		pp=true;
	}
	return 0;
}
void dfs(int p)
{
	bool jx=false;
	for(int j=1;j<=n;j++)
	{
		if(vis[j]>=2)
			continue;
		if(yc[p][j]==0)
			continue;
		if(yc[p][j]==tr[p].size()||yc[p][j]==tr[j].size())
			continue;
		an+=tr[j].size()-yc[p][j];
		vis[j]++;
		jx=true;
		dfs(j);
		an-=tr[j].size()-yc[p][j];
		vis[j]--;
	}
	if(jx==false)
		ans=max(ans,an);
	return;
}
int main()
{
	cin>>n;
	for(int i=1;i<=n;i++)
		cin>>tr[i];
	cin>>ch;
	for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
			yc[i][j]=mt(i,j);
	for(int i=1;i<=n;i++)
		if(tr[i][0]==ch)
		{
			vis[i]++;
			an=tr[i].size();
			dfs(i);
			vis[i]=0;
		}
	cout<<ans<<endl;
	return 0;
}