class Solution {
public:
    int minOperations(vector<int>& nums) {
        map<int,int>mp;

        for(auto i:nums)
        {
            mp[i]++;
        }
        priority_queue<int>pq;

        for(auto i:mp)
        {
            pq.push(i.second);
        }
        int res = 0;
        while(!pq.empty())
        {
            auto tp = pq.top();
            pq.pop();

            if(tp > 4)
            {
                pq.push(tp-3);
            }
            else if(tp  == 4)
            {
                pq.push(tp-2);
            }
            else if(tp != 3 && tp != 2)
            {
                return -1;
            }
            res++;
        }
        return res;
    }
};
