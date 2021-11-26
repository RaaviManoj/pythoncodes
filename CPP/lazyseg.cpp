// $ Author @CAP_10
#include<bits/stdc++.h>
#include<ctime>
#include<chrono>
using namespace std;
// $ Just believe in yourself
 
 
 
//@ Defining the the shortcuts for long words
#define ull unsigned long long
#define ll long long
#define ld long double
#define ar array
#define vt vector
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define sz(x) (int)(x).size()
#define ff first
#define ss second
#define mp make_pair
#define mt make_tuple

int n;
const int mxN=8e5;

vt<ll> arr;
ull tree[mxN+1] = {0}; 
ull lazy[mxN+1] = {0}; 

ll mi(ll l, ll r){
    return l+(r-l)/2;
}

void build(int l=1, int r=n, int ind = 1 ){
    if (l==r){
        tree[ind]=arr[l-1];
        return;
    }
    ll mid=mi(l,r);
    build(l, mid, 2*ind);
    build(mid+1, r, 2*ind+1);
    tree[ind]=tree[2*ind]+tree[2*ind+1];
}

void update(int qs, int qe, ll val, int l=1, int r=n, int ind=1){
    
    if (lazy[ind]!=0){
        tree[ind]+=(r-l+1)*lazy[ind];
        if (l!=r){
            lazy[2*ind]+=lazy[ind];
            lazy[2*ind+1]+=lazy[ind];
        }
        lazy[ind]=0;
    }

    if (qs>r || l>r || qe<l)
        return;
    if (qs<=l && r<=qe){
        tree[ind]+=(r-l+1)*val;
        if (l!=r){
            lazy[2*ind]+=val;
            lazy[2*ind+1]+=val;
        }
        return;
    }
    ll mid=mi(l,r);
    update(qs, qe, val, l, mid, 2*ind);
    update(qs, qe, val, mid+1, r, 2*ind+1);
    tree[ind]=tree[2*ind]+tree[2*ind+1];
}

ull query(int qs, int qe, int l=1, int r=n, int ind=1){
    if (lazy[ind]!=0){
        tree[ind]+=(r-l+1)*lazy[ind];
        if (l!=r){
            lazy[ind*2]+=lazy[ind];
            lazy[2*ind+1]+=lazy[ind];
        }
        lazy[ind]=0;
    }
    if (qs>r || qe<l || l>r)
        return 0;
    if (l>=qs && r<=qe)
        return tree[ind];
    ll mid=mi(l,r);
    return query(qs, qe, l, mid, 2*ind)+query(qs, qe, mid+1, r, 2*ind+1);
}
